# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from datetime import datetime

from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    ordering = "create_time"
    template_name = "news/post_list.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    template_name = "news/post_details.html"
    context_object_name = "post"
