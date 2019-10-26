from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})