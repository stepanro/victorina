from django.urls import path
from .views import VictorinaView

urlpatterns = [
    path('button/', VictorinaView.as_view(), name='button'),
]