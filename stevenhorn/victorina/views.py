from django.shortcuts import render
from django.http import HttpResponse

def button(requests):
    return render(requests, 'victorina/index.html')
