import html
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import random
import re

def sovet():
    ran = random.choice([i for i in range(1, 5)])
    r = requests.get('https://howcarworks.ru/лайфхак?page={}'.format(ran)).text

    s = BeautifulSoup(r, 'lxml')

    links = s.find_all('span', 'field-content')
    links_new = []
    for i in links:
        a = i.find('a').get('href')
        a = unquote(a)
        links_new.append('https://howcarworks.ru' + a)

    ran2 = random.choice([i for i in range(1, 13)])
    try:
        r2 = requests.get(links_new[ran2]).text
    except IndexError:
        r2 = requests.get(links_new[0]).text

    s2 = BeautifulSoup(r2, 'lxml')
    title = s2.find('h1').text.strip()
    body_list = s2.find_all('div', 'field field-name-body field-type-text-with-summary field-label-hidden')
    body = ''
    for i in body_list:
        i = i.text.strip()
        i = i.replace('\n', '')
        body += i
    body = body.split()
    body = ' '.join(body)
    return str(title) + '📌' + '\n' + str(body) + '🤔'


def photo():
    c = 0
    while c ==0:
        try:
            url = 'https://auto.vercity.ru/catalog/auto/'

            page = requests.get(url, verify=False)

            s = BeautifulSoup(page.text, 'lxml')
            ls = s.find('ul', 'popular-brands').text.strip().split()
            ls_new = [i.lower() for i in ls if len(i) > 1 and i.isalpha()]
            cars = random.sample(ls_new, k=4)
            car = cars[0]
            print(car)
            cat_hist = requests.get(url + car.lower() + '/history.htm', verify=False)

            s_h = BeautifulSoup(cat_hist.text, 'lxml')
            # print(url + car.lower() + '/history.htm')
            hist_page = s_h.find('div', 'page_history-text').text.strip()
            # print(hist_page)

            img_page = requests.get('https://auto.vercity.ru/gallery/automobiles/{}/'.format(car), verify=False)
            # print('https://auto.vercity.ru/gallery/automobiles/{}/'.format(car))
            s_img = BeautifulSoup(img_page.text, 'lxml')
            links = s_img.find('ul', 'section_galleries-type1')
            ddd = re.findall(r'gallery\/automobiles.+\"', str(links))
            ddd_l = []
            for i in ddd:
                i = i[: len(i)-1]
                ddd_l.append('https://auto.vercity.ru/' + i)

            int_ = random.choice([i for i in range(0, 7)])
            cat_photo = ddd_l[int_]
            r2 = requests.get(cat_photo, verify=False)
            s2_img = BeautifulSoup(r2.text, 'lxml')
            img_link = s2_img.find('div', 'block_wrap-img')
            img = 'https://auto.vercity.ru' + img_link.find('img').get('src')
            img = img.replace(' ', '%20')
            c += 1
            return {'img': img, 'true': car, 'false1': cars[1], 'false2': cars[2], 'false3': cars[3]}
        except Exception as e:
            print('ERROR!!!!!!!!', e)
            continue
