from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .filters import PostFilter
from .forms import PostCreateForm, PostEditForm, SubscriptionEditForm

from .models import Post
from .tasks import send_new_post_mail

# from .mailer import send_new_post_mail #! deprecated in d7.5


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

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)

        new_post = self.object
        # send_new_post_mail(new_post)
        send_new_post_mail.delay(new_post.pk)
        return result


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


class SubscriptionUpdate(LoginRequiredMixin, View):
    def get(self, request):
        form = SubscriptionEditForm(instance=request.user)
        return render(
            request=request,
            template_name="news/subscription_edit.html",
            context={
                "form": form,
            },
        )

    def post(self, request):
        form = SubscriptionEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render(
            request=request,
            template_name="news/subscription_edit.html",
            context={
                "form": form,
                "message": "Подписка успешно сохранена",
            },
        )
