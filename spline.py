# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate

# importing data from file data_int.py
import data_int
# creating simpler names for variables
x = data_int.x
y = data_int.y

# array containing the points where we want to evaluate the 
# intepolation
x_int = np.linspace(0,1,num=64)

# generate linear interpolant 
f_lin = interpolate.interp1d(x, y, kind='linear')
# evaluate linear interpolan at the desiderd points
y_int_lin = f_lin(x_int)

# generate spline interpolant 
f_spline  = interpolate.splrep(x, y, s=0)
# evaluate spline interpolan at the desiderd points
y_int_spline = interpolate.splev(x_int, f_spline, der=0)

# plot results
plt.figure()
plt.plot(x,y,'gh',ms=10)
plt.plot(x_int,y_int_lin,'r.',x_int,y_int_spline,'b.')
plt.xlabel('x')
plt.ylabel('y')

# plot a zoom
plt.figure()
plt.plot(x,y,'gh',ms=10)
plt.plot(x_int,y_int_lin,'r.',x_int,y_int_spline,'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0.05,0.3)
plt.ylim(0.5,1.5)

plt.show()
