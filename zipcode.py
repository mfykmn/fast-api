import requests
import json

url = "https://zipcloud.ibsnet.co.jp/api/search"

zip = input("郵便番号を入力=>")

param = {"zipcode": zip}

res = requests.get(url, param)

data = json.loads(res.text)

print(data)

print('*' * 50)

if data['results'] is not None:
    address_info = data['results'][0]
    zipcode = address_info['zipcode']
    address = f"{address_info['address1']}{address_info['address2']}{address_info['address3']}"
    print(f"郵便番号: {zipcode} 住所: {address}")
else:
    print("住所情報が見つかりませんでした")