import time
import os
import requests

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


def get_status(user_id):
    data = {
        'user_ids': user_id,
        'v': '5.110',
        'access_token': os.getenv('access_token_vk'),
        'fields': 'online'
    }
    response = requests.post(
        'https://api.vk.com/method/users.get', params=data
        ).json()['response'][0]
    return response['online']


def sms_sender(sms_text):
    client = Client(
        os.getenv('account_sid'),
        os.getenv('auth_token')
    )
    message = client.messages.create(
        to=os.getenv('NUMBER_TO'),
        from_=os.getenv('NUMBER_FROM'),
        body=sms_text
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
