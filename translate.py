import requests
import os
from dotenv import load_dotenv

load_dotenv()

# https://cloud.yandex.ru/docs/translate/operations/translate
# Платно!

# IAM_TOKEN надо обновлять не реже чем раз в 12 часов
# https://cloud.yandex.ru/docs/iam/operations/iam-token/create

IAM_TOKEN = os.getenv('IAM_TOKEN')
folder_id = os.getenv('YC_FOLDER')


def translate(texts, language):
    body = {
        "targetLanguageCode": language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
    )
    return response.json()
