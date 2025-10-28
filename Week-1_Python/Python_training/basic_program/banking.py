'''
Date:28-10-2025
Author: Omkar
Description: Banking Interest calculations
'''

from mypackage.module_int_cal import simple_interest,compound_interest

prin = float(input('Principal amount: '))
ny = float(input('Number of years: '))
roi = float(input('Rate of interest: '))

si,amt = simple_interest(prin=prin, ny=ny, roi=roi)
print(f'Simple Interest: {si} Amount: {amt}')

ci,amt=compound_interest(prin=prin, ny=ny, roi=roi)
print(f'Compound Interest: {ci} Amount: {amt}')
