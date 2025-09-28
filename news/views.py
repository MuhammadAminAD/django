from django.shortcuts import render
from django.views.generic import ListView

from news.models import PostModel


# Create your views here.

class PostsList(ListView):
    model = PostModel
    template_name = "home.html"
