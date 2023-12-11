# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:17:07 2023

@author: rober
"""

import numpy as np
from scipy.optimize import minimize

# Given expression to minimize
def objective(variables):
    x, y = variables
    return -(-20*1.2*np.sin(x) - 30*1.2*np.sin(x) - 30*1.5*np.sin(y))

# Initial guess
initial_guess = [0, 0]

# Perform optimization to find the minimum
result = minimize(objective, initial_guess, bounds=[(-np.pi, np.pi), (-np.pi, np.pi)])

# Extract the minimum value and corresponding values of x and y
min_value = -result.fun
x_min, y_min = result.x

print(f"The minimum value is {min_value} at (x, y) = ({x_min}, {y_min})")
