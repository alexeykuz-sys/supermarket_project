"""
favourites url
"""
from django.urls import path
from . import views

urlpatterns = [
    path('<product_id>/', views.favourites, name='favourites'),

    path('', views.product_favourite_list, name='product_favourite_list'),

]
