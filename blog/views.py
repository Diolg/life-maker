from django.shortcuts import render

# Create your views here.
from .models import Post

# Create your views here.
def blog(request):
   
    return render(request, 'blog/blog.html')

