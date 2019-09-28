import requests
import os
import argparse
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN_BITLY')

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Ваша ссылка' )
    return parser

def shorten_link(token, url):
    server_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    data = {"long_url": url}
    response_post = requests.post(server_url, json=data, headers=headers)
    response_post.raise_for_status()
    response_dict = response_post.json()
    return response_dict['link']


def count_clicks(token, link):
    server_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link.strip("http://")}/clicks/summary'
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "units": -1,
        "unit": "day"
    }
    response = requests.get(server_url, params=params, headers=headers)
    response.raise_for_status()
    response_dict = response.json()
    return response_dict['total_clicks']

if __name__ == "__main__":
    parser = createParser()
    user_input = parser.parse_args().link

    if user_input.startswith('http://bit.ly/'):
        try:
            bitlink_clicks = count_clicks(TOKEN, user_input)
        except requests.exceptions.HTTPError:
            print('Неправильная ссылка')
        print('Число переходов: ', bitlink_clicks)
    else:
        try:
            bitlink = shorten_link(TOKEN, user_input)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:
            print('Неправильная ссылка')
