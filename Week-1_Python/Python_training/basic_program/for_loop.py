'''
Date:25-10-2025
Author: Omkar
Description: Using for loop
'''
terms=int(input("Enter Terms:"))
sum=0
for num in range(1,terms+1):
    sum+=num*num
print(f'The sum is: {sum}')