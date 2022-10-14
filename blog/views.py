from django.shortcuts import render
from .models import Post
from django.http import Http404
# Create your views here.
def list(request):
    Data = {'Post': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)
    '''''
def post(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/post.html', {'post' : post})
'''

def post(request, id):
    try:
        post_data = Post.objects.get(id = id)
    except Post.DoesNotExist:
        raise Http404("The post des not exist.")
    return render(request, 'blog/post.html', {'post':post_data})