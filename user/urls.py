from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('createpost', views.create_post, name="createpost"),
    path('viewposts', views.PostsView.as_view(), name="viewposts")
]
