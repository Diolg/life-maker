from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import CommentForm
from .models import Post


def blog(request):
    posts = Post.objects.all()
   
    return render(request, 'blog/blog.html', {'posts': posts})

@login_required
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else: 
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

