# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.interpolate import interp1d
import numpy as np
from scipy.optimize import minimize

x = np.array([-30,0,30])

y = np.array([6870, 6728, 6615])

f1 = interp1d(x,y, kind='quadratic')

result = minimize(f1, 0)
