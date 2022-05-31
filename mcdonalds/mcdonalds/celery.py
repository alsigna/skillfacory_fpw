import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcdonalds.settings")

app = Celery("mcdonalds")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "print_every_5_seconds": {
        "task": "board.tasks.printer",
        # "schedule": 5, # every 5 sec
        "schedule": crontab(hour=13, minute=5),  # UTC time
        "args": (5,),
    },
}
