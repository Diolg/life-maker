from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
            messages.error(request, "Nothing in your cart at the moment")
            return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J2a6dBT1Oh2RAY3PGMBi3WAnnNMiFxZ1UOsmvopYFbZzSt8XrztdBWc0LWdwN4W4yS33U1lL0a9HerOHx5G2KZh00wwydSVdF',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)



