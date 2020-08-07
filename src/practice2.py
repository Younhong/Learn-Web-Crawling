import requests

url = "http://domeggook.com/main/item/itemList.php"

params = {
    'sfc': 'ttl',
    'sf': 'ttl',
    'sw': 'galaxy',
    'pg': '2'
}

res = requests.get(url, params=params)

print(res.text)
print(res.url)
