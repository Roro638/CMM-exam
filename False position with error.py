# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:23:09 2023

@author: rober
"""

MAX_ITER = 1000000

def degfunc( x ):
    return (x**2 + 5*x -4)
    

def Code( a , b):
    if degfunc(a) * degfunc(b) >= 0:
        print("You have not assumed correct values of a and b")
        return 0
    c = a

    for i in range(MAX_ITER):
        c_old = c
        c = (a * degfunc(b) - b * degfunc(a))/ (degfunc(b) - degfunc(a))
        error = (abs(c - c_old) / c) * 100
        print(error)
        if degfunc(c) == 0:
            break
        elif degfunc(c) * degfunc(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : " , '%.4f' %c)
    
Code(0,1)