# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math


# ------------------------------------------------------
# functions that returns dy/dx
# i.e. the equation we want to solve
def model(y,x):
    dydx = y*(1.0-y)
    return dydx
# ------------------------------------------------------

# ------------------------------------------------------
# inputs
# initial conditions
x0 = 0
y0 = math.exp(-4)/(math.exp(-4) + 1)
# total solution interval
x_final = 10
# ------------------------------------------------------

h_values = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1, 2, 5])
RMQE_eul = np.zeros(len(h_values))
RMQE_rk  = np.zeros(len(h_values))

for hh in range(0,len(h_values)):

         # ------------------------------------------------------
         # step size
         h = h_values[hh]
         # number of steps
         n_step = math.ceil(x_final/h)
         # ------------------------------------------------------
         
         # ------------------------------------------------------
         # Euler method
         
         # Definition of arrays to store the solution
         x_eul = np.zeros(n_step+1)
         y_eul = np.zeros(n_step+1)
         e_eul = np.zeros(n_step+1)
         
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
         # ------------------------------------------------------
         
         
         # ----------------------------------------------------
         # ------------------------------------------------------
         
         
         # ------------------------------------------------------
         # Compute error
         e_eul = y_eul - np.exp(x_eul-4)/(np.exp(x_eul-4) + 1)         
         # Root mean square error
         # ------------------------------------------------------
         
         # ------------------------------------------------------
         # very refined sampling of the exact solution c*e^(-x)
         # n_exact linearly spaced numbers
         # only needed for plotting exact solution
         
         # Definition of array to store the exact solution
         n_exact = 1000
         x_exact = np.linspace(0,x_final,n_exact+1) 
         y_exact = np.zeros(n_exact+1)
         
         # exact values of the solution
         for i in range(n_exact+1):
             y_exact[i] = math.exp(x_exact[i]-4)/(math.exp(x_exact[i]-4) + 1)
         # ------------------------------------------------------
         
         # ------------------------------------------------------
         # plot results in the loop
         plt.figure()
         plt.plot(x_eul, y_eul , 'b.-', label='Eul')
         plt.plot(x_exact, y_exact , 'r-', label='Exact')
         plt.xlabel('x')
         plt.ylabel('y(x)')
         st1 = 'Solution for h = '+str(h) 
         plt.legend(title=st1)
         st2 = 'Solution_h_'+str(h)+'.pdf'
         plt.savefig(st2)
         
         plt.figure()
         plt.plot(x_eul, e_eul , 'b.-', label='Eul')
         plt.xlabel('x')
         plt.ylabel('error(x)')
         st1 = 'Error for h = '+str(h) 
         plt.legend(title=st1)
         st2 = 'Error_h_'+str(h)+'.pdf'
         plt.savefig(st2)
         # ------------------------------------------------------


# ------------------------------------------------------
# plot outside the loop
plt.figure()
plt.loglog(h_values, 0.1*h_values , 'b-', label='h^1')
plt.loglog(h_values, 1e-3*h_values**4.0 , 'g--', label='h^4')
plt.xlabel('h')
plt.ylabel('RMQE')
st1 = 'Error vs h'
plt.legend(title=st1)
st2 = 'Error_vs_h.pdf'
plt.savefig(st2)

# ------------------------------------------------------

         
#plt.show()


