import os

from YandexImagesParser.ImageParser import YandexImage
from utils import download_file_by_url

parser = YandexImage()


def get_image_list(text, limit=25):
    result = []
    for item in parser.search(text)[:limit]:
        data = item.__dict__
        del data['preview']
        result.append(data)
    return result


def download_image_list(text, folder, limit=25):
    data = get_image_list(text)
    if not os.path.exists(folder):
        os.mkdir(folder)
    counter = 0
    for item in data:
        url = item['url']
        filename = url.split('/')[-1]
        filepath = '/'.join([folder, filename])
        try:
            download_file_by_url(url, filepath)
            counter += 1
            if counter >= limit:
                break
        except Exception:
            continue
