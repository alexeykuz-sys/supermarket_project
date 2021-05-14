from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from reviews.models import Review
from products.models import Product
from profiles.models import UserProfile
from .forms import ReviewForm

# Create your views here.


def review_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(
        product=product, date_lte=timezone.now().order_by('-date'))
    context = {
        'product': product,
        'reviews': reviews,
    }
    
    return render(request,reviews.html, context)

def add_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.user = UserProfile.objects.get(user=request.user)
                data.product = product
                data.save()
                return redirect(reverse('product_detail', args=(product_id,)))
        else:
            form = ReviewForm()
        return redirect(reverse('product_detail', args=(product_id,)))
    else:
        return redirect('profiles/profile.html')