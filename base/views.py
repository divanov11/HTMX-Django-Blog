from django.shortcuts import render
from base.models import Post
from django.http import HttpResponse

def index(request):
    post = Post.objects.first()
    context = {'post':post}
    return render(request, 'index.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render(request, 'index.html', context)