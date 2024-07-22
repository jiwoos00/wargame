import hashlib

str = "test"
res = hashlib.md5(str.encode()).hexdigest()
print(res)
