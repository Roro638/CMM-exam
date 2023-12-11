# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:34:29 2020

@author: emc1977
"""
import numpy as np
import matplotlib.pyplot as plt

def calculate_dx (a, b, n):
	return (b-a)/float(n)

def rect_rule (f, a, b, n):
	total = 0.0
	dx = calculate_dx(a, b, n)
	for k in range (0, n):
        	total = total + f((a + (k*dx)))
	return dx*total

def f(x,p):
    return (np.sin(x)*np.cos(p*x))



solution = rect_rule(f,0,np.pi,100)
print(rect_rule(f, 0, 3.14, 10000))
