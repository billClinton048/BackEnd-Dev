from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index , name = "view"),
    path("", views.home , name = "home")
]