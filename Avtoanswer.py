import requests
import json

def Bot_info(data):
    data = data['result']
    for i in data:
        user_id = i['message']['from'].get('id')
        user_text = i['message'].get('text')
    url = 'https://api.telegram.org/bot5462386389:AAFy5Zz73zUqpEjcsNSJ3J1rmFh4sWl-Y08/sendMessage'
    r = requests.get(url, params={'chat_id':user_id, 'text':user_text})

url = 'https://api.telegram.org/bot5462386389:AAFy5Zz73zUqpEjcsNSJ3J1rmFh4sWl-Y08/getUpdates'
r = requests.get(url)
h = r.json()
x = Bot_info(h)