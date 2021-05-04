from django.urls import path
from . import views 

urlpatterns = [
    path('', views.view_favourite, name='view_favourite'),
    path('add/<item_id>/', views.add_to_favourite, name='add_to_favourite'),
   
   
]
