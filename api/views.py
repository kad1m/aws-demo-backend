from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def apiresponse(request):
    return HttpResponse('Hello, World for React!')
