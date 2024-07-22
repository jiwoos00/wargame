import requests

url = "https://webhacking.kr/challenge/js-1/?291600"
cookie = {'PHPSESSID':'o54emhtlvf2o49nhb20475ja2l'}

ul = url.find(".kr")
ul = int(ul) * 30

params = {'input_pwd':ul}
res = requests.post(url, cookies = cookie, data = params)
print(res.text)
