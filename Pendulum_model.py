import numpy as np
"""
Here the gravitational constant 
(meters per second) is defined
"""
g = 9.8

def Euler_equations(dt, t):
    """
    In this function we calculate values of x and alpha on the
    next step
    """
    x += dt*v
    alpha += dt*omega
    return x, alpha

def RK_4(dt, t):
    """
    Here we calculate the value of velocity and angle-velocity
    on the next iteration
    """
    phi = A4*t**4 + B*t**3 + C*t**2 + D*t + E
    phi_prime = 4*A4*t**3 + 3*B*t**2 + 2*C*t + D 
    phi_dprime = 12*A4*t**2 + 6*B*t + 2*C
    v += dt*(A*(np.sin(phi)*(phi_prime)**2 - np.cos(phi)*phi_dprime)
    - b*v + omega**2*(x + A*np.sin(phi)) - g*np.cos(phi) + k*(x - x0))
    omega += dt*(g*np.sin(alpha) - omega*k*(x + A*sin(phi)) - 2*omega*(x + A*np.cos(phi)*phi_prime))/(x + A*np.sin(phi))
    return v, omega