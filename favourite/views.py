from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib import messages

# Create your views here.
def view_favourite(request):
    
    """ A view that renders the bag contents page """
    
    return render(request, 'favourite/favourite.html')


def add_to_favourite(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url')
    
    if product.favourite.filter(product_id).exist():
        product.favourite.remove(request.user)
    else:
        product.favourite.add(request.user)
        print(product.favourite)
    
    return redirect(redirect_url)
