from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

def get_index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render (request, 'index.html' ,{'posts': posts})


def new_post(request):
	pass