import requests
import info

res = requests.get(info.url + "/challenge/web-28?val=1 procedure analyse()", cookies = info.cookies)
print(res.text)
