from django.urls import path
from .views import blogcreate, blog_list

urlpatterns = [
    path('',blogcreate , name='blog-create'),
    path('list/', blog_list, name='blog-list'),
    ]
