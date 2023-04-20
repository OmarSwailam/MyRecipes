import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myrecipes.settings")

celery = Celery("myrecipes")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()
