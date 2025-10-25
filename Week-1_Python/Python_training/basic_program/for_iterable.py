'''
Date:25-10-2025
Author: Omkar
Description: Using for iterable
'''
num=[10,20,30,40,50]
sq_num=[]
for i in num:
    print(i)
    sq_num.append(i*i)
print(sq_num)


tup_sq=tuple(sq_num)
print(tup_sq)
set_sq=set(sq_num)
print(set_sq)


dnum=dict()
num1=[1,2,3,4,5]
for n in num1:
    dnum[n]=n*n
print(dnum)
for k,v in dnum.items():
    print(f'{k}:{v}')

for k in dnum.keys():
    print(k)
