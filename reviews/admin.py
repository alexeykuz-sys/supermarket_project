from django.contrib import admin
from reviews.models import Review


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'date_added'
        

    )



admin.site.register(Review, ReviewsAdmin)