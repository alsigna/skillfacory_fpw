import logging

import pytz
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone, translation
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .filters import PostFilter
from .forms import PostCreateForm, PostEditForm, SubscriptionEditForm
from .models import Category, Post
from .tasks import send_new_post_mail

logger = logging.getLogger(f"django.NewsPaper.{__name__}")
logger_template = logging.getLogger("django.template")
logger_security = logging.getLogger("django.security")
logger_server = logging.getLogger("django.server")


# from .mailer import send_new_post_mail #! deprecated in d7.5


class Index(View):
    def get(self, request):
        string = _("Hello world")
        categories = Category.objects.all()

        context = {
            "string": string,
            "categories": categories,
            "current_time": timezone.now(),  # текущая TZ
            "timezones": pytz.common_timezones,  #  добавляем в контекст все доступные TZ
        }
        return HttpResponse(
            render(
                request=request,
                context=context,
                template_name="news/lang.html",
            ),
        )

    def post(self, request):
        request.session["django_timezone"] = request.POST["timezone"]
        return HttpResponseRedirect(reverse("lang_index"))


class PostList(ListView):
    model = Post
    ordering = "create_time"
    template_name = "news/post_list.html"
    context_object_name = "posts"
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        logger.debug("debug-message")
        logger.info("info-message")
        logger.warning("warning-message")
        logger_security.info("security info message")
        logger_server.error("test error message for email")
        try:
            raise Exception("fake exception for logging")
        except Exception as exc:
            logger.critical(str(exc), exc_info=exc.__traceback__)
            logger_template.critical(str(exc), exc_info=exc.__traceback__)
        return super().get(request, *args, **kwargs)


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

    def get_object(self, *args, **kwargs):
        pk = self.kwargs["pk"]
        obj = cache.get(f"post-{pk}")

        if not obj:
            print(f"post-{pk} NOT in cache")
            obj = super().get_object(queryset=self.queryset)
            cache.set(f"post-{pk}", obj)
        else:
            print(f"post-{pk} in cache")
        return obj


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
