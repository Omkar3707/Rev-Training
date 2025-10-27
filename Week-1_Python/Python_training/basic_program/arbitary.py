'''
Date:27-10-2025
Author: Omkar
Description: Using Arbitary arguments
'''
def add(*args):
    total=0
    for num in args:
        total+=num
    return total

print(add(1,2,3,4,5,6))
print(add(5,8,6,7))
def calculate(m1,m2,m3):
    '''

    :param m1:
    :param m2:
    :param m3:
    :return:
    '''

    total=m1+m2+m3
    avg=total/3
    return total,avg
sname=input("Enter your  name: ")
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
#pylint: disable=invalid-name
Total,Avg=calculate(n1,n2,n3)
print(f"Name: {sname} The sum is: {Total} and average is: {Avg}")
