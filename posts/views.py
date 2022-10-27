from django.shortcuts import render
from posts.models import Post

# Create your views here.

def register(request):
    return render(request, 'register1.html')


def index(request):
    posts = Post.objects.all ()
    context = {
        'posts' : posts
    }
    return render (request, 'index.html', context)
