from django.urls import path
from .views import *

urlpatterns = [
    path('', victorina),
    path('admin/', admin),
]