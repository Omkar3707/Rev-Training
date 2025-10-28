'''
Date:28-10-2025
Author: Omkar
Description: My calculations
'''

from mypackage.module_int_cal import simple_interest
from mypackage.shape_cal import area_of_circle,area_of_rectangle

prin = float(input('Principal amount: '))
ny = float(input('Number of years: '))
roi = float(input('Rate of interest: '))

print(f'Simple Interest: {simple_interest(prin=prin, ny=ny, roi=roi)[0]} '
      f'Amount: {simple_interest(prin=prin, ny=ny, roi=roi)[1]}')

print(f'Area of Circle: {area_of_circle(5)}\n'
      f'Area of Rectangle: {area_of_rectangle(5,2)}')
