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
        product=product_id).order_by('-date_added')
    context = {
        'product': product,
        'title': title,
        'reviews': reviews,
        
    }
    
    return render(request,reviews.html, context)

def add_review(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.title = request.POST['title']
                form.comment = request.POST['comment']
                form.user = UserProfile.objects.get(user=request.user)
                form.product = product
                form.save()
                return redirect(reverse('product_detail', args=(product_id,)))
                
            
        else:
            form = ReviewForm()
        return redirect(reverse('product_detail', args=(product_id,)))
    else:
        return redirect('home/index.html')
    
    
@login_required
def edit_review(request,product_id, review_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        review = Review.objects.get(product=product, pk=review_id)
        
        if request.user == review.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, instanct=review)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.save()
                    return redirect(reverse('product_detail', args=(product_id),))   
            else:
                form = ReviewForm(instance=review)
            return redirect('reviews/edit_review.html', {'form':form})
        else:
            return redirect(reverse('product_detail', args=(product_id),))
    else:
        return redirect('home/index.html')
        


@login_required
def delete_review(request, product_id):
    """ Delete a review from the product view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, product_id)
    
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=(product_id,)))
