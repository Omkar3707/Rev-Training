'''
Date:25-10-2025
Author: Omkar
Description: Using Functions
'''
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
sum=add(n1,n2)
print(sum)
a=10
b=5
print(sub(a,b))
print(sub(n1=b,n2=a))


def addition(*adds):
    sum=0
    for num in adds:
        sum+=num
    return sum
n1=2
n2=1
n3=5
n4=9
n5=8
print(addition(n1,n2))
print(addition(n1,n3,n4))
print(addition(n1,n2,n3,n4))
print(addition(n1,n2,n3,n4,n5))
