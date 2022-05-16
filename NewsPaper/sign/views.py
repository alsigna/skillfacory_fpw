from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView

from .forms import UserForm


class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        form = UserForm(instance=user)
        return render(
            request=request,
            template_name="sign/profile.html",
            context={
                "form": form,
                "is_author": user.groups.filter(name="author").exists(),
            },
        )

    def post(self, request):
        user = User.objects.get(pk=request.user.pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
        return render(
            request=request,
            template_name="sign/profile.html",
            context={
                "form": form,
                "is_author": user.groups.filter(name="author").exists(),
            },
        )


class BaseRegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("login")


@login_required
def upgrade_author(request):
    user = request.user
    author_group = Group.objects.get(name="author")
    if not request.user.groups.filter(name="author").exists():
        author_group.user_set.add(user)
    return redirect(reverse("profile"))


@login_required
def downgrade_author(request):
    user = request.user
    author_group = Group.objects.get(name="author")
    if request.user.groups.filter(name="author").exists():
        author_group.user_set.remove(user)
    return redirect(reverse("profile"))
