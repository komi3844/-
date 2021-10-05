import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


URL = 'https://helpdesk.zakupki.gov.ru/secure/Dashboard.jspa'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'Accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tbody', class_='ui-sortable')

    cart = []
    for item in items:
        cart.append({
            'title': item.find('div', class_='registry-entry__header-mid__number').get_text(strip=True),
            'name': item.find('div', class_='registry-entry__body-href').get_text(strip=True),
            'link': item.find('div', class_='registry-entry__body-href').get('href')
        })
    print(cart)

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-8 pr-0 mr-21px')

    cart = []
    for item in items:
        cart.append({
            'title': item.find('div', class_='registry-entry__header-mid__number').get_text(strip=True),
            'name': item.find('div', class_='registry-entry__body-href').get_text(strip=True),
            'link': item.find('div', class_='registry-entry__body-href').get('href')
        })
    print(cart)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
