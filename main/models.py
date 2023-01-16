from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=100,decimal_places=2)
    quantity = models.IntegerField
