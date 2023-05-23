import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/new/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


# GET, POST, DELETE, PUT, PATCH
def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="b-content__inline_item", limit=5)
    parsed_data = []
    for item in items:
        info = item.find('div', class_='b-content__inline_item-link').find('div').string.split(', ')
        parsed_data.append({
            "title": item.find('div', class_='b-content__inline_item-link').find('a').getText(),
            "url": item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            "year": info[0],
            "country": info[1],
            "genre": info[2],
            "status": item.find('span', class_='info').string
            if item.find('span', class_='info') else "Полнометражка",
            "img": item.find("img").get('src')
        })
    return parsed_data


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        parsed_data = get_data(html.text)
        return parsed_data
    raise Exception("Ошибка в парсере!")

