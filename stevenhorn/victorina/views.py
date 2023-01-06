from ast import Dict
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import os
import requests
from dotenv import load_dotenv
import json


load_dotenv()

def api_requests(step, count):
    api_key = os.getenv("API_KEY")
    print(api_key)

    req_str = f'https://engine.lifeis.porn/api/millionaire.php?qType={step}&count={count}&apikey={api_key}'
    responce = requests.get(req_str)

    responce = json.loads(responce.text)

    print(responce)

    # with open(file='responce.json', mode='w', encoding='utf-8') as write_responce:
    #     json.dump(responce, write_responce, indent=4, ensure_ascii=False)

    return responce['data'][0]['question'], responce['data'][0]['answers']

    # with open(file='victorina/responce.json', mode='r', encoding='utf-8') as read_responce:
    #     responce = json.load(read_responce)
    #     return responce['data'][0]['question'], responce['data'][0]['answers']

        # print(responce['data'][0]['question'])
        # print(responce['data'][0]['answers'])
        # print(responce['amount'])


class VictorinaView(TemplateView):
    template_name = 'victorina/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        responce = api_requests(step=1, count=1)
        
        api_requests_question = responce[0]
        api_requests_answer = responce[1]
        context['api_requests_question'] = api_requests_question
        context['api_requests_answer'] = api_requests_answer

        return context
