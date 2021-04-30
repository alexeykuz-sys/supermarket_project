from django.urls import path
from . import views 

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('products_favourite/<product_id>/', views.products_favourite, name='products_favourite'),
   
]
