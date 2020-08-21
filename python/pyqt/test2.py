# -*- coding: utf-8 -*-
import requests

from requests import RequestException
import re
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36'}


def get_index_html():
    gonglv_url = 'http://www.mafengwo.cn/jd/10195/gonglve.html'
    try:
        response = requests.get(gonglv_url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_index_url(index_html):
    pattern = re.compile('<a.*?href="(/poi.*?)".*?', re.S)
    urls = re.findall(pattern, index_html)
    for url in urls:
        url = 'https://m.mafengwo.cn' + url
        yield url
    return url


def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_html(html):
    doc = pq(html)
    title = doc('div.title').text()
    details = doc('div.row.h1').text()

   # for i in range(len(details)):
        #print(details[i])
    restult = {
        'title': title,
        'details': details




    }

    print(restult)


def main():
    index_html = get_index_html()
    for index_url in get_index_url(index_html):
        html = get_html(index_url)
        if html:
            #                print(html)
            parse_html(html)


if __name__ == '__main__':
    main()


