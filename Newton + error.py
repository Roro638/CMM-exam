import math
import numpy as np
import matplotlib.pyplot as plt

errors = []

def newton(f,Df,x0,epsilon,max_iter):
    
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        x_new = xn - fxn/Dfxn
        error = abs(((x_new - xn)/xn))
        errors.append(error)
        print(f"Iteration {n}: Approximate root = {x_new}, Error = {error}%")
        
        xn = x_new
    print('Exceeded maximum iterations. No solution found.')
   
    return None

f = lambda x: x**2 + 4*x - 12
df= lambda x: 2*x + 4
x0=16
epsilon=0.001
max_iter=100
solution = newton(f,df,x0,epsilon,max_iter)
print(solution)

x1 = np.arange(0,5,1)
f1 = x1**2+4*x1-12
plt.plot(x1,errors, 'o-')
plt.grid()
plt.show()