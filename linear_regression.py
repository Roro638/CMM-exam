# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate

# importing data from file data_reg.py
import data_reg
# creating simpler names for variables
x = data_reg.x
y = data_reg.y

# array containing the points where we want
# to evaluate the fit
x_fit = np.linspace(0,1,num=64)


# ----------------------------------------------------
# Linear regression using least squares 
# with formulas presented in Lecture

n = len(x)
a_1 = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n * np.sum(x**2) - (np.sum(x))**2)
a_0 = np.mean(y) - a_1*np.mean(x) 

# evaluate the linear regression at the desired points 
y_reg_lin = a_0 + a_1 * x_fit 

# Print coefficients of linear regression:
print('Coefs a_1 and a_0 (our implementation): ', a_1,a_0)
# ----------------------------------------------------

# ----------------------------------------------------
# Linear regression using python functions

# compute the coefficients for the linear regression
coef = np.polyfit(x,y,1)
# generate the linear function that fits the data 
f_reg_lin = np.poly1d(coef)

# evaluate the linear regression at the desired points 
y_reg_lin_py = f_reg_lin(x_fit)

# Print coefficients of linear regression:
print('Coefs a_1 and a_0 (python function): ', coef)
# ----------------------------------------------------


# plot results
plt.figure()
plt.plot(x,y,'gh',ms=5)
plt.plot(x_fit,y_reg_lin,'b-')
plt.xlabel('x')
plt.ylabel('y')

plt.figure()
plt.plot(x,y,'gh',ms=5)
plt.plot(x_fit,y_reg_lin_py,'r-')
plt.xlabel('x')
plt.ylabel('y')


plt.show()
