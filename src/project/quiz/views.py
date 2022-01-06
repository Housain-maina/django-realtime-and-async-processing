from django.shortcuts import render


def index(request):

    return render(request, 'quiz/index.html', context={'text': 'hello world'})
