from django.urls import path
from .views import IndexView, NewOrderView, take_order, HelloView

urlpatterns = [
    path("", IndexView.as_view()),
    path("hello/", HelloView.as_view(), name="hello"),
    path("new/", NewOrderView.as_view(), name="new_order"),
    path("take/<int:oid>", take_order, name="take_order"),
]
