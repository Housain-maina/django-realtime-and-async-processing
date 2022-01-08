import requests
import json
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()


@shared_task
def get_quiz():
    url = 'https://opentdb.com/api.php?amount=1&category=18&difficulty=medium&type=boolean'
    response = requests.get(url).json()
    question = response['results'][0]['question']
    incorrect_answer = response['results'][0]['incorrect_answers'][0]
    correct_answer = response['results'][0]['correct_answer']
    options = [correct_answer, incorrect_answer]

    quiz = json.dumps({'question':  question, 'options': options})

    async_to_sync(channel_layer.group_send)('quiz', {'type': 'send_quiz', 'text': quiz})
