import requests
from bs4 import BeautifulSoup as bs

url = "http://www.diablock.co.jp/nanoblock/en/catalog"

res = requests.get(url)

soup = bs(res.text, 'html.parser')

urls_row = soup.find('ul', {'id': 'product'}).find_all('a')

for u in urls_row:
    detail_item = u['href']
    res2 = requests.get(detail_item)
    soup2 = bs(res2.text, 'html.parser')

    name = soup2.find('span', {'class': 'roboto light'}).text
    thumb = soup2.find('div', 'thumb imgbox').find('img')['src']
    details = soup2.find('div', {'class': 'info table'}).text

    print(name)
    print(thumb)
    print(details)
