from django.urls import path
from main import views


urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('blog/<int:blog_id>/', views.blog_details, name="blog-details"),
    path('signup/', views.signup, name="signup")

]
