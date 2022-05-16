from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, upgrade_author, downgrade_author

from .views import ProfileUpdate

urlpatterns = [
    path("login/", LoginView.as_view(template_name="sign/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="sign/logout.html"), name="logout"),
    path("profile/", ProfileUpdate.as_view(), name="profile"),
    path("signup/", BaseRegisterView.as_view(template_name="sign/signup.html"), name="signup"),
    path("upgrade/", upgrade_author, name="upgrade"),
    path("downgrade/", downgrade_author, name="downgrade"),
]
