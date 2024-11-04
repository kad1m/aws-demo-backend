from django.urls import path
from .views import index, apiresponse
urlpatterns = [
    path('', index),
    path('ping/', apiresponse),
]