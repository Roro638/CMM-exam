import math
import numpy as np
import matplotlib.pyplot as plt

def bisection(f,a,b,N):
      
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
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
            print("Bisection method fails.")
            return None
        
        true_pi = np.pi
        error = abs((m_n - true_pi)/true_pi)*100
        print(f"Iteration {n}: Approximate root = {m_n}, Error = {error}%")
        
    return (a_n + b_n)/2

f = lambda x: (x/10)*np.cosh(10*50/x) + 5 -x/10 - 15
approx_phi = bisection(f,1264,1267,100)
print(approx_phi)

