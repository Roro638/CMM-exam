import math
import numpy as np
import matplotlib.pyplot as plt

errors = []

def secant(f,a,b,N):
   
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    m_old = a_n
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
        error = 1-abs((m_n - m_old)/m_old)*100
        errors.append(error)
        print(errors)
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

f = lambda x: 115000 * x * (1 + x)**6 / ((1 + x)**6 - 1) - 25500
solution = secant(f,0.05,0.5,1000)
print(solution)

# Plotting the function
x_values = np.arange(0, 4, 0.1)
f_values = x_values**2 + 4*x_values - 12
plt.plot(x_values, f_values)
plt.grid(True)
plt.show()
