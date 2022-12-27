from django.urls import path
from .views import *

urlpatterns = [
    path('button/', button),
    path('test/', button),
]