from django.urls import path, re_path

from .views import (
    PostCreate,
    PostDelete,
    PostDetail,
    PostList,
    PostSearch,
    PostUpdate,
    SubscriptionUpdate,
    Index,
)

# from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("lang/", Index.as_view(), name="lang_index"),
    # path("<int:pk>", cache_page(30)(PostDetail.as_view()), name="post_detail"),
    path("<int:pk>", PostDetail.as_view(), name="post_detail"),
    path("<int:pk>/edit", PostUpdate.as_view(), name="post_edit"),
    path("<int:pk>/delete", PostDelete.as_view(), name="post_delete"),
    path("search/", PostSearch.as_view(), name="post_search"),
    path("create/", PostCreate.as_view(), name="post_create"),
    path("subscribe/", SubscriptionUpdate.as_view(), name="subscription_update"),
]
