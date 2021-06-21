from django.shortcuts import render
from .models import Product

# Create your views here.
def all_sessions(request):
    """ A view to return all sessions and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/sessions.html', context) 


