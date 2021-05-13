from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def reviews(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    
    
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def add_review(request):
    """ Add a review to the product """

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            review_content = form.cleaned_data.get("review_content")
            Review.objects.create(user=user,
                                  product=get_object_or_404(Product, pk=product_id),
                                  review_content=review_content)
            review = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add review. '
                            'Please ensure the form is valid.'))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)



@login_required
def edit_review(request, product_id):
    """ Edit a product in the store """
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update review. '
                            'Please ensure the form is valid.'))
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id):
    """ Delete a product from the store """
    review = get_object_or_404(Review, pk=review_id)
    product = get_object_or_404(Product, pk=product_id)
    review.delete()
    product.save()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_details'))