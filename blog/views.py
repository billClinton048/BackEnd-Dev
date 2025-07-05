from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Blog_Home view 
def blog_home(request):
    posts  = BlogPost.objects.all().order_by('-published_at')
    return render(request, 'blog_home.html', {'posts': posts})

# cfeating blogs vies 
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = BlogPostForm()

    return render(request, 'create_post.html', {'form': form })