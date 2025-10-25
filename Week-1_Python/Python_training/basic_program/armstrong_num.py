'''
Date:25-10-2025
Author: Omkar
Description: Checking Armstrong Number
'''
numstr=input('Enter a number: ')
numlen=len(numstr)
num=int(numstr)
temp=num
sum=0
while num>0:
    rem=num%10
    sum+=rem**numlen
    num//=10
if temp==sum:
        print(f'{temp} is Armstrong Number')

else:
        print(f'{temp} is not Armstrong Number')
for i in range(10):
    print(i)
