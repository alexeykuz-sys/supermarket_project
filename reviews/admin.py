from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'form',
        'reviews',

    )

    ordering = ('-reviews',)


admin.site.register(Review, ReviewsAdmin)