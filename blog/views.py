from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_list(request):
    names = ['Oleg', 'Masha', 'Olja']
    return render(request, 'blog/index.html', context={'names': names})