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

f = lambda x: (x / 10)* np.cosh((10*50)/x) + 5 - x / 10
df= lambda x: np.sinh(10*50/x)
x0=0.1
epsilon=0.001
max_iter=100
solution = newton(f,df,x0,epsilon,max_iter)
print(solution)



