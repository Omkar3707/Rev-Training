'''
Date:28-10-2025
Author: Omkar
Description: Module for Interest calculations
'''

def simple_interest(prin,ny,roi):
    """
    Calculating simple interest
    :param prin: Principal amount
    :param ny: number of years
    :param roi: rate of interest
    :return:
    """
    si=prin*ny*roi/100
    amount=prin+si
    return si,amount
def compound_interest(prin,ny,roi):
    '''
    Calculating compound interest
    :param prin: principal amount
    :param ny: number of years
    :param roi: rate of interest
    :return:
    '''
    amount=prin*(1+(roi/100))**ny
    ci=amount - prin
    return ci,amount
