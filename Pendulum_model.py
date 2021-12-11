import numpy as np
"""
Here the gravitational constant 
(meters per second) is defined
"""
g = 9.8

def Euler_equations(dt, pend):
    """
    In this function we calculate values of x and alpha on the
    next step
    """
    pend.x0 += dt*pend.v0
    pend.alpha0 += dt*pend.w0

def RK_4(dt, t, pend):
    """
    Here we calculate the value of velocity and angle-velocity
    on the next iteration
    """
    phi = pend.A4*t**4 + pend.B*t**3 + pend.C*t**2 + pend.D*t + pend.E
    phi_prime = 4*pend.A4*t**3 + 3*pend.B*t**2 + 2*pend.C*t + pend.D 
    phi_dprime = 12*pend.A4*t**2 + 6*pend.B*t + 2*pend.C
    pend.v0 += dt*(pend.A*(np.sin(phi)*(phi_prime)**2 - np.cos(phi)*phi_dprime)
    - pend.mu_m*pend.v + pend.w0**2*(pend.x0 + pend.A*np.sin(phi)) - g*np.cos(phi) + pend.k*(pend.x - pend.x0))
    pend.w0 += dt*(g*np.sin(pend.alpha0) - pend.w0*pend.k*(pend.x + pend.A*np.sin(phi)) 
    - 2*pend.w0*(pend.x + pend.A*np.cos(phi)*phi_prime))/(pend.x + pend.A*np.sin(phi))

