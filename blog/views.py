from django.shortcuts import render
from django.db import DatabaseError, DataError
from .models import BlogPost


# Create your views here.
def index(request):
    context = {
        "blog_data": BlogPost.objects.all()
    }
    return render(request, 'blog/index.html', context)


def blog_page(request, blog_id):
    try:
        blog_data = BlogPost.objects.get(pk=blog_id)
    except:
        blog_data = None
    context = {
        "blog_data": blog_data
    }
    return render(request, 'blog/blog.html', context)