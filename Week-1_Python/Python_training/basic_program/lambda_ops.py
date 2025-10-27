'''
Date:27-10-2025
Author: Omkar
Description: Using Lambda function
'''

num=[1,2,3,4]
square=list(map(lambda x: x**2,num))
print (square)
var=lambda x,y:2*x+3*y+7
print(var(4,5))
# pylint: disable=invalid-name
str1='Hello'
for ch in str1:
    print(ch)
s=iter(str1)
print(next(s))
print(next(s))
