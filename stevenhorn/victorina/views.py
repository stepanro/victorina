from ast import Dict
from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.views import View
import os
import requests
from dotenv import load_dotenv
import json
from .forms import LoginForm
from .models import *


load_dotenv()

def api_requests(step, count):
#     api_key = os.getenv("API_KEY")
#     print(api_key)

#     req_str = f'https://engine.lifeis.porn/api/millionaire.php?qType={step}&count={count}&apikey={api_key}'
#     responce = requests.get(req_str)

#     responce = json.loads(responce.text)

#     print(responce)

    # with open(file='responce.json', mode='w', encoding='utf-8') as write_responce:
    #     json.dump(responce, write_responce, indent=4, ensure_ascii=False)

    # return responce['data'][0]['question'], responce['data'][0]['answers']

    with open(file='stevenhorn/victorina/responce.json', mode='r', encoding='utf-8') as read_responce:
        responce = json.load(read_responce)
        return responce['data'][0]['question'], responce['data'][0]['answers']

        # print(responce['data'][0]['question'])
        # print(responce['data'][0]['answers'])
        # print(responce['amount'])


class LoginCreateView(CreateView):
    model = Person
    template_name = "victorina/login.html"
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')
    fields = '__all__'




# class VictorinaView(TemplateView):
#     template_name = 'victorina/index.html'
#     success_url = reverse_lazy('button')
#     login_url = reverse_lazy('button')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         responce = api_requests(step=1, count=1)
        
#         api_requests_question = responce[0]
#         api_requests_answer = responce[1]
#         context['api_requests_question'] = api_requests_question
#         context['api_requests_answer'] = api_requests_answer

#         return context

def victorina(request):
    context = dict()
    model = Person
    responce = api_requests(step=1, count=1)
    api_requests_question = responce[0]
    api_requests_answer = responce[1]

    context['api_requests_question'] = api_requests_question
    context['api_requests_answer'] = api_requests_answer

    return render(request=request, template_name='victorina/index.html', context=context)