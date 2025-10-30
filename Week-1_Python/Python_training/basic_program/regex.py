import re

txt="Hello ! My number is 8765345642"
pat="123456"
res=re.search(r'\d',txt)
num=re.findall(r'\d{10}',txt)
r=re.split(r"!",txt)
print(num)
print(res)
print(r)