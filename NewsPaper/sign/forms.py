# from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User


class UserForm(UserCreationForm):
    # email = forms.EmailField(label="email")
    # first_name = forms.CharField(label="first_name")
    # last_name = forms.CharField(label="last_name")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# class BaseRegisterForm(UserCreationForm):
#     email = forms.EmailField(label="Email")
#     first_name = forms.CharField(label="Имя")
#     last_name = forms.CharField(label="Фамилия")

#     class Meta:
#         model = User
#         fields = (
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#         )
