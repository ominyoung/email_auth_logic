from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailAuthLogic.settings')

# Celery App 생성
app = Celery('EmailAuthLogic')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Seoul')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.autodiscover_tasks()


# Celery task 생성
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')