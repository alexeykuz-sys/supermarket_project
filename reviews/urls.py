from django.urls import path
from . import views 

urlpatterns = [
    path('<int:product_id>/', views.review_list, name='review_list'),
    path('addreview/<int:product_id>/', views.add_review, name='add_review'),
    path('editreview/<int:product_id>/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:product_id>/', views.delete_review, name='delete_review'),
]