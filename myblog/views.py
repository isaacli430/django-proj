from django.shortcuts import render, get_object_or_404
from .models import Post, Author

# Create your views here.

def posts_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'myblog/posts/index.html', context)

def posts_show(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.filter(author__id = post.author.id)
    context = {'post': post, 'posts': posts}
    return render(request, 'myblog/posts/show.html', context)

def authors_index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'myblog/authors/index.html', context)

def authors_show(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author__id = author.id)
    context = {'author': author, 'posts': posts}
    return render(request, 'myblog/authors/show.html', context)

def home(request):
    return render(request, 'myblog/home.html')