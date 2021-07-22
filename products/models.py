from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'products'
