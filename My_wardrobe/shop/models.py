from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=450)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class FeatProduct(models.Model):
    IsFiction = models.BooleanField(default=True)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=450, default="")
    product_price = models.IntegerField(default=0)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class contactus(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    tel = models.CharField(max_length=15, default="")
    desc = models.CharField(max_length=450, default="")

    def __str__(self):
        return self.name

