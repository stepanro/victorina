from django.shortcuts import render
from django.http import HttpResponse

def victorina(requests):
    return HttpResponse('Это страница викторины!')

def admin(requests):
    return HttpResponse('админка')