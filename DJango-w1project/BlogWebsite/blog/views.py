from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Post
from .models import Comment
from .models import Category

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def users(request):
  myusers = User.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))

def udetails(request, uid):
  myuser = User.objects.get(uid=uid)
  template = loader.get_template('udetails.html')
  context = {
    'myuser': myuser,
  }
  return HttpResponse(template.render(context, request))

def blogs(request):
  myblogs = Post.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
    'myblogs': myblogs,
  }
  return HttpResponse(template.render(context, request))

def pdetails(request, pid):
    myblog = get_object_or_404(Post, pid=pid)
    comments = Comment.objects.filter(post_id=myblog).order_by('date_posted')
    template = loader.get_template('blogdetails.html')
    context = {
        'myblog': myblog,
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def comments(request, post_id):
  mycomments = Comment.objects.all().values()
  template = loader.get_template('comments.html')
  context = {
    'mycomments': mycomments,
  }
  return HttpResponse(template.render(context, request))

def categories(request):
  mycategories = Category.objects.all().values()
  template = loader.get_template('categories.html')
  context = {
    'mycategories': mycategories,
  }
  return HttpResponse(template.render(context, request))
