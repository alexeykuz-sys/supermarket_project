"""
This script renders review admin
"""
from django.contrib import admin
from reviews.models import Review


class ReviewsAdmin(admin.ModelAdmin):
    """
    creates class of review with admin
    """
    list_display = (
        'product',
        'user',
        'date_added',
        'title',
        'comment',
    )

admin.site.register(Review, ReviewsAdmin)
