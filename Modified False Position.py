# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:52:51 2020

@author: emc1977
"""


"""
Created on Tue Jul 28 09:51:32 2020

@author: emc1977
"""

import numpy as np
import matplotlib.pyplot as plt
# Python3 implementation of Bisection 
# Method for solving equations 
  
MAX_ITER = 1000000
  
# An example function whose solution 
# is determined using Bisection Method.  
# The function is x^3 - x^2 + 2 
def func( x ): 
    return (x**2+5*x-4) 


# Prints root of func(x) in interval [a, b] 
def regulaFalsi( a , b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
    c = a # Initialize result 
    c_old = 0 
    for i in range(MAX_ITER): 
          
        # Find the point that touches x axis 
        c = (a * 0.5*func(b) - b * func(a))/ (0.5*func(b) - func(a)) 
        error = abs(((c - c_old)/c)*100)
        print(error)
        # Check if the above found point is root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c
        c_old = c
    print("The value of root is : " , '%.4f' %c) 
    print(i)
    
# Driver code to test above function 
# Initial values assumed 
a =-7
b =0
regulaFalsi(a, b) 
  
x = np.arange(-10,10,0.1)
f1 = x**2+5*x-4
plt.plot(x,f1)
plt.grid()
# This code is contributed by "Sharad_Bhardwaj". 

