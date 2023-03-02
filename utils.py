import requests


def download_file_by_url(url, file_to):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_to, 'wb') as f:
            for chunk in r.iter_content(256):
                f.write(chunk)
    else:
        raise Exception(f'Запрос завершился некорректно и вернул статус {r.status_code}')