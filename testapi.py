import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

# api_key = os.getenv("API_KEY")
# print(api_key)

# req_str = f'https://engine.lifeis.porn/api/millionaire.php?qType=1&count=1&apikey={api_key}'
# responce = requests.get(req_str)

# responce = json.loads(responce.text)

# with open(file='responce.json', mode='w', encoding='utf-8') as write_responce:
#     json.dump(responce, write_responce, indent=4, ensure_ascii=False)

with open(file='responce.json', mode='r', encoding='utf-8') as read_responce:
    responce = json.load(read_responce)

    print(responce['data'][0]['question'])
    print(responce['data'][0]['answers'])
    print(responce['amount'])
