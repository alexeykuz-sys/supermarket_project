from django.urls import path
from . import views 

urlpatterns = [
    path('<int:product_id>/', views.review_list, name='review_list'),
    path('addreview/<int:product_id>/', views.add_review, name='add_review'),
]