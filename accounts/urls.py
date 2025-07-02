from django.urls import path
from . import views


print("urlPatters loDED")
# Paths
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('success/', views.success, name = 'success'),
]