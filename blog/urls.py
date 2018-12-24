# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name =  "blog/blog.html")),
                   url('(?P<pk>(\d+))', DetailView.as_view(model = Post, template_name = "blog/post.html")),
                  ]
