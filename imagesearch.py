import requests
import json
from bs4 import BeautifulSoup
import base64


def yasearch(src):
    with open(src, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": '###',
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        data = res.text
        a = json.loads(data.replace("'", '"'))
        url = r'https://yandex.ru/images/search?source=collections&rpt=imageview&url={}'.format(a['data']['url'])

        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        similar = soup.find('a',
                            class_='Button2 Button2_size_l Button2_type_link Button2_view_default Button2_width_auto Tags-Item')

        try:
            s = similar.text.upper()
        except AttributeError:
            s = 'Не могу понять, что на фото :('

    return s
