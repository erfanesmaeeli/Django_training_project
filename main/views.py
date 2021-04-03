from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Blog


def home(request):
    ctx = {}
    if request.user.is_authenticated:
        ctx["name"] = request.user.get_full_name()
    else:
        ctx["name"] = False
    all_blogs = Blog.objects.all()
    ctx["blogs"] = all_blogs
    return render(request, "blog.html", ctx)





