from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile


from django.conf import settings

# Create your views here.

@login_required
def favourites(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    
    if product.favourites.filter(id=request.user.id).exists():
        product.favourites.remove(request.user)
    else:
        product.favourites.add(request.user)
        
    
    return redirect(reverse('product_detail', args=[product.id]))

@login_required
def product_favourite_list(request):
    user=request.user
    favourite_products = user.favourites.all()
    
    context = {
        'is_favourite': favourite_products
    }

    return render(request, 'favourites/product_favourite_list.html', context)
    