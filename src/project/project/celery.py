import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_quiz_3s': {
        'task': 'quiz.tasks.get_quiz',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()
