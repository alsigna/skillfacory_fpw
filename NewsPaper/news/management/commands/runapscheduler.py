import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from NewsPaper.private_settings import EMAIL_FROM

from news.models import Category

logger = logging.getLogger(__name__)


def _send_weekly_mail(posts, category) -> None:
    for user in category.subscribers.all():
        if user.email == "" or user.email is None:
            return

        html_content = render_to_string(
            "news/email/weekly_posts.html",
            {
                "category": category,
                "posts": posts,
                "user": user,
            },
        )

        msg = EmailMultiAlternatives(
            subject=f"New posts in {category.category} for this week.",
            body=html_content,
            from_email=EMAIL_FROM,
            to=[user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


def my_job():
    for category in Category.objects.all():
        posts = category.post_set.filter(create_time__gte=datetime.now() - timedelta(minutes=3600))
        if posts.count() != 0:
            _send_weekly_mail(posts, category)
    print("job done")


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(minute="*/1"),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
