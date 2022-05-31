import time
from datetime import datetime, timedelta

from celery import shared_task

from .mailer import _send_mail, _send_weekly_mail
from .models import Category, Post


@shared_task
def hello():
    time.sleep(2)
    print("Hello, world!")


@shared_task
def send_new_post_mail(post_id: int) -> None:
    post = Post.objects.get(pk=post_id)
    if post is None:
        return
    for category in post.category.all():
        for user in category.subscribers.all():
            _send_mail(post, category, user)


@shared_task
def send_weekly_mail():
    for category in Category.objects.all():
        posts = category.post_set.filter(create_time__gte=datetime.now() - timedelta(minutes=3600))
        if posts.count() != 0:
            _send_weekly_mail(posts, category)
    print("summary mails were sent")
