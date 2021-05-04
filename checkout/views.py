from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag=request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return(redirect(reverse('products')))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form':order_form,
        'stripe_public_key': 'pk_test_51IbNAFGOFACUw6CtTX0Qx7HIzeVHXnwSCkClhhvUg78b32EYQzLV80rdQAwh7lC20x4kmtrrda4pyp0dAErn1DZL009mEDoAV7',
        'client_secret': 'test client secret'
    }
    
    return render(request, template, context)