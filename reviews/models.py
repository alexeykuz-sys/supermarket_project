from django.db import models
from profiles.models import UserProfile
from products.models import Product
from django.utils import timezone



class Review(models.Model):

    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey( UserProfile, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank = False, default ='')
    comment = models.CharField(max_length=200, blank = False, default ='')
    date_added = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.comment
