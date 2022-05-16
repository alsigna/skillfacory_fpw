from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User


class UserForm(UserCreationForm):
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


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name="common")
        basic_group.user_set.add(user)
        return user
