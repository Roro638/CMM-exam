# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# functions that returns dy/dx
# i.e. the equation we want to solve: dy_j/dx = f_j(x,y_j) (j=[1,2] in this case)
def nonlinear_model(x,y_1,y_2):
    g = 9.81
    l = 9.81
    f_1 = y_2
    f_2 = -g/l*np.sin(y_1)
    return [f_1 , f_2]
# ------------------------------------------------------
def linear_model(x,y_1,y_2):
    g = 9.81
    l = 9.81
    f_1 = y_2
    f_2 = -g/l*y_1
    return [f_1 , f_2]

# ------------------------------------------------------
# initial conditions
x0 = 0
y0_1 = np.pi/4
y0_2 = 0
# total solution interval
x_final = 30
# step size
h = 0.01
# ------------------------------------------------------


# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_1_eul = np.zeros(n_step+1)
y_2_eul = np.zeros(n_step+1)
y_1_eul_linear = np.zeros(n_step+1)
y_2_eul_linear = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_1_eul[0] = y0_1
y_2_eul[0] = y0_2
y_1_eul_linear[0] = y0_1
y_2_eul_linear[0] = y0_2
x_eul[0]   = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    [slope_1 , slope_2] = nonlinear_model(x_eul[i],y_1_eul[i],y_2_eul[i]) 
    # use the Euler method
    y_1_eul[i+1] = y_1_eul[i] + h * slope_1
    y_2_eul[i+1] = y_2_eul[i] + h * slope_2
    print(y_1_eul[i],y_2_eul[i])
# ------------------------------------------------------
for i in range(n_step):
    # compute the slope using the differential equation
    [slope_1_linear , slope_2_linear] = linear_model(x_eul[i],y_1_eul_linear[i],y_2_eul_linear[i]) 
    # use the Euler method
    y_1_eul_linear[i+1] = y_1_eul_linear[i] + h * slope_1_linear
    y_2_eul_linear[i+1] = y_2_eul_linear[i] + h * slope_2_linear
    print(y_1_eul_linear[i],y_2_eul_linear[i])

# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_1_eul , 'b.-',x_eul, y_2_eul , 'r-', x_eul, y_1_eul_linear, x_eul, y_2_eul_linear)
plt.xlabel('x')
plt.ylabel('y_1(x), y_2(x)')
plt.show()
# ------------------------------------------------------
for i in range (len(x_eul)):
    values = [10, 20, 30]
    if round(x_eul[i],5) in values:
        print(x_eul[i], y_1_eul[i], y_1_eul_linear[i], y_2_eul[i], y_2_eul_linear[i])
# ------------------------------------------------------
# ------------------------------------------------------

