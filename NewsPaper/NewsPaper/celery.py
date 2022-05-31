import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPaper.settings")

app = Celery("NewsPaper")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send_summary_every_tuesday": {
        "task": "news.tasks.send_weekly_mail",
        "schedule": crontab(minute="*/5", day_of_week="Tuesday"),  # UTC time
    },
}
