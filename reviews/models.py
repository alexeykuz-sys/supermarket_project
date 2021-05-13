from django.db import models
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    reviews = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    review_content = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add = True)
    
    
    def get_review_content(self):
        return self.review_content