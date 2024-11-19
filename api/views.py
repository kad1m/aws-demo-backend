import os

from django.shortcuts import render, HttpResponse
from dotenv import load_dotenv

load_dotenv()


def index(request):
    text = os.getenv('MESSAGE_DJANGO')
    return render(request, 'index.html', {'text': text})


def apiresponse(request):
    text = os.getenv('MESSAGE_REACT')
    return HttpResponse('Hello, World for React!')
