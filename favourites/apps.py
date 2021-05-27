"""
This register favourite app in apps
"""
from django.apps import AppConfig


class FavouriteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favourites'
