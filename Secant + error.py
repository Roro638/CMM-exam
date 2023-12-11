import math
import numpy as np
import matplotlib.pyplot as plt

errors1 = []

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
        error = 100-abs((m_n - m_old)/m_old)*100
        errors1.append(error)
        print(errors1)
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

f = lambda x: x**2 + 4*x - 12
solution = secant(f,1,4,25)
print(solution)

plt.plot(range(1, len(errors1) + 1), errors1, marker='o')
plt.xlabel('Iteration')
plt.ylabel('Relative Error')
plt.title('Relative Error vs Iteration in Secant Method')
plt.grid(True)
plt.show()

# Plotting the function
x_values = np.arange(0, 4, 0.1)
f_values = x_values**2 + 4*x_values - 12
plt.plot(x_values, f_values)
plt.grid(True)
plt.show()
