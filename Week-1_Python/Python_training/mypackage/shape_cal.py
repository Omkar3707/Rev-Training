'''
Date:28-10-2025
Author: Omkar
Description: Area, Circumference of square, rectangle, circle
'''

from math import pi

def area_of_square(size):
    '''
    Function to calculate area of square
    :param size: side length of square
    :return: Area of square
    '''

    return size*size

def area_of_circle(rad):
    '''
    function to calculate area of circle
    :param rad: radius of circle
    :return: Area of circle
    '''
    return pi*rad*rad

def area_of_rectangle(len,brd):
    '''
    function to calculate area of rectangle
    :param len: length of rectangle
    :param brd: breadth of rectangle
    :return: area of rectangle
    '''
    return len*brd

def circumference_of_circle(rad):
    '''
    function to calculate circumference of circle
    :param rad: radius of circle
    :return: circumference of circle
    '''
    return 2*pi*rad
