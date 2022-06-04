from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from NewsPaper.private_settings import EMAIL_FROM

from .models import Post


@receiver(post_delete, sender=Post)
def send_delete_mail(sender, instance, **kwargs) -> None:
    admin = User.objects.get(username="admin")
    send_mail(
        subject=f"post has been deleted",
        message=f"post has been deleted:\n {instance.preview}",
        from_email=EMAIL_FROM,
        recipient_list=[admin.email],
    )


@receiver(pre_save, sender=Post)
def check_daily_rate(sender, instance, **kwargs):
    post_count = Post.objects.filter(
        author=instance.author,
        create_time__gte=datetime.now() - timedelta(days=1),
    ).count()
    if post_count > 3:
        raise PermissionDenied("you can not publish more than 3 posts")
