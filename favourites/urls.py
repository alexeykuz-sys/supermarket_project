from django.urls import path
from . import views 

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('favourites/', views.product_favourite_list, name='product_favourite_list'),
  
   
]
