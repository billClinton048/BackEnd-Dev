from django.urls import path 
from . import views 

# paths 
urlpatterns = [
    path('blog_home/', views.blog_home, name = 'blog_home'),
    path('create_blog', views.create_post, name = 'create_post')
]