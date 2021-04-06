from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Blog
from django.urls import reverse
from .forms import SignUpForm, SignUpForm2
from django.contrib.auth.models import User
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm2(request.POST)
        if form.is_valid():
            user = form.save()
            phonenumber = form.cleaned_data['phone']
            user.refresh_from_db()
            user.profile.phone = phonenumber
            user.save()
            messages.success(request, 'کاربر جدید با موفقیت ایجاد گردید.')
            return HttpResponseRedirect(reverse('signup'))

    else:
        form = SignUpForm2()
    return render(request, "signup.html", {"form": form})

    
def blog(request):
    ctx = {}
    if request.user.is_authenticated:
        ctx["name"] = request.user.get_full_name()
    else:
        ctx["name"] = False
    all_blogs = Blog.objects.all()
    ctx["blogs"] = all_blogs
    return render(request, "blog.html", ctx)



def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "blog_details.html", {"blog": blog})
