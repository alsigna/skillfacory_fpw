from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from NewsPaper.private_settings import EMAIL_FROM

from .models import Category, Post


def _send_mail(post: Post, category: Category, user: User) -> None:
    if user.email == "" or user.email is None:
        return

    html_content = render_to_string(
        "news/email/new_post.html",
        {
            "category": category,
            "post": post,
            "user": user,
        },
    )
    msg = EmailMultiAlternatives(
        subject=f"New post in {category.category}",
        body=html_content,
        from_email=EMAIL_FROM,
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    # send_mail(
    #     subject=f"new post in {category.category}",
    #     message=post.preview + ":" + post.get_absolute_url(),
    #     from_email=EMAIL_FROM,
    #     recipient_list=[user.email],
    # )


def send_new_post_mail(post: Post) -> None:
    for category in post.category.all():
        for user in category.subscribers.all():
            _send_mail(post, category, user)
