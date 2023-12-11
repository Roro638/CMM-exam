# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    l = -10
    dydx = l*y + (1-l)*np.cos(x)-(1+l)*np.sin(x)
    return dydx

# initial conditions
x0 = 0
y0 = 1
# total solution interval
x_final = 4*np.pi
# step size

h_values = [0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
# ------------------------------------------------------
# ------------------------------------------------------
# Euler method
for h in h_values:
# number of steps
    n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
    y_eul = np.zeros(n_step+1)
    x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
    y_eul[0] = y0
    x_eul[0] = x0 

# Populate the x array
    for i in range(n_step):
        x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
    for i in range(n_step):
    # compute the slope using the differential equation
        slope = model(y_eul[i],x_eul[i]) 
    # use the Euler method
        y_eul[i+1] = y_eul[i] + h * slope  

# plot results

    N = len(x_eul)
    error = np.zeros(N)
    real_y = np.zeros(N)
    
    for i in range(1,len(x_eul)):
        real_y[i] = np.sin(x_eul[i]) + np.cos(x_eul[i])
        error[i] = np.abs(((y_eul[i] - real_y[i]) / y_eul[i])) * 100
    
    plt.plot(x_eul, y_eul, 'b.', x_eul, real_y, 'r')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.show()
    # ------------------------------------------------------
    
    for i in range (len(x_eul)):
        values = [6.28, 12.566]
        if round(x_eul[i],5) in values:
            print(x_eul[i], y_eul[i])
    
    max_error = max(error)
    print(max(error))
    print(f"For h = {h}: Max True Error: {max_error}")
