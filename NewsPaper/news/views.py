import django
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .filters import PostFilter
from .forms import PostCreateForm, PostEditForm
from .models import Post


class PostList(ListView):
    model = Post
    ordering = "create_time"
    template_name = "news/post_list.html"
    context_object_name = "posts"
    paginate_by = 3


class PostSearch(PostList):
    template_name = "news/post_search.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filterset"] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "news/post_details.html"
    context_object_name = "post"


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("news.add_post",)
    form_class = PostCreateForm
    model = Post
    template_name = "news/post_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_url"] = reverse("post_list")
        return context


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("news.change_post",)
    form_class = PostEditForm
    model = Post
    template_name = "news/post_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_url"] = reverse("post_detail", kwargs={"pk": self.get_object().pk})
        return context


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ("news.delete_post",)
    model = Post
    template_name = "news/post_delete.html"
    success_url = reverse_lazy("post_list")
    context_object_name = "post"
