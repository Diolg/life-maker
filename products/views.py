from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_sessions(request):
    """ A view to return all sessions and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/sessions.html', context)


def session_detail(request, product_id):
    """ A view to show individual session details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/session_detail.html', context)  


