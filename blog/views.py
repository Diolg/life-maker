from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm, PostForm
from .models import Post



def blog(request):
    posts = Post.objects.all()
   
    return render(request, 'blog/blog.html', {'posts': posts})

@login_required
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not request.user:
            messages.error(request,
                           'Sorry, only registered shoppers can do that.')
            return redirect(reverse('blog'))

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else: 
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


