from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginCreateView.as_view(), name='login'),
    path('button/', victorina, name='button'),
]