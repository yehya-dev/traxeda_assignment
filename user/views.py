from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import Registration, CreatePost
from django.contrib.auth import login as login_user, authenticate, logout as logout_user
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from . import models
# Create your views here.


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login_user(request, user)
            messages.success(request, "Registration succesful")
            return redirect('user:homepage')
        messages.error(request, "Unsuccesssful registration. Invalid information.")
    form = Registration()
    return render(request=request, template_name='user/register.html', context={'register_form': form})    

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if redirect_url := request.GET.get('next'):
                    return redirect(redirect_url)
                else:
                    return redirect("user:homepage")
            else:
                messages.error(request, "invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name='user/login.html', context={'login_form': form})

def logout(request):
    logout_user(request)
    messages.info(request, "You have succesfully logged out.")
    return redirect("user:homepage")

@login_required(login_url=reverse_lazy('user:login'))
def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            post = models.Post.create_post(request, text)
            if post:
                messages.info(request, f"Created new post.")
                return redirect('user:viewposts')
            else:
                messages.error(request, f"Could not create a post.")
        else:
            messages.error(request, f"Could not create a post.")
    else:
        form = CreatePost()
        return render(request=request, template_name='user/create_post.html', context={'post_form':form})      

class PostsView(ListView):
    model = models.Post

def homepage(request):
    return render(request=request, template_name='user/homepage.html')
