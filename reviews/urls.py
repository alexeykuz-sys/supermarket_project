from django.urls import path
from . import views 

urlpatterns = [
    path('addreview/<int:product_id>/', views.add_review, name='add_review'),
    path('edit_review/<int:product_id>/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:product_id>/<int:review_id>/', views.delete_review, name='delete_review'),
]