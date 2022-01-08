from django.urls import path
from . consumers import QuizConsumer

ws_urlpatterns = [
    path('ws/quiz/', QuizConsumer.as_asgi()),
]
