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
    v += dt*(A*(np.sin(phi(t))*(phi_prime(t))**2 - np.cos(phi(t))*phi_dprime(t))
    - b*v + omega**2*(x + A*np.sin(phi(t))) - g*np.cos(phi(t)) + k*(x - x0))
    omega += dt*(g*np.sin(alpha) - omega*k*(x + A*sin(phi(t))) - 2*omega*(x + A*np.cos(phi(t))*phi_prime(t)))/(x + A*np.sin(phi(t)))

    return v, omega