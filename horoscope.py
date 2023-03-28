import requests

# https://www.ohmanda.com/api/horoscope/


def get_horoscope(sign):
    resp = requests.get(f'https://ohmanda.com/api/horoscope/{sign.lower()}')
    if resp.status_code != 200:
        raise Exception('Horoscope failed, check your sign or connection')
    return resp.json()['horoscope']