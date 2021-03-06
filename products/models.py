"""
products models
"""
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    creates category class
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
    This script creates category friendly name
    """
        return self.friendly_name




class Product(models.Model):
    """
    creates produtc class
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True,
                                blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)

    def __str__(self):
        return self.name
