from django.shortcuts import render
from django.http import HttpResponse

def button(request):
    return render(request, 'victorina/index.html')
