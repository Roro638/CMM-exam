# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:57:03 2020

@author: emc1977
"""

import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

x = np.arange(0,10,100)
y = x**2+4*x-12
plt.plot(x,y)

u = 1.8 * 10**3
m0 = 160*10**3
q = 2.5*10**3
t = np.arange(0,30,0.1)
v = u * np.log(m0/(m0-q*t))

x0 = 0; x1 = 1;
y0 = u * np.log(m0/(m0-q*x0)); y1 = u * np.log(m0/(m0-q*x1));
plt.fill_between([x0,x1],[y0,y1])

plt.xlim([0,30]); plt.ylim([0,2000]);
plt.show()

A = 0.5*(y1 + y0)*(x1 - x0)
print("Trapezoid area:", A)

def trapz(f,a,b,N=1000):
    
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

def f(x):
    return u * np.log(m0/(m0-q*x))

print(trapz(f,0,30,1000))