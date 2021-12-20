from numpy import sin, cos
"""
Here the gravitational constant 
(meters per second) is defined
"""
g = 10000

def Euler_equations(pend, t, dt):
    """
    In this function we calculate values of x and alpha on the
    next step
    """
    phi = pend.A4*t**4 + pend.B*t**3 + pend.C*t**2 + pend.D*t + pend.E
    phi_prime = 4*pend.A4*t**3 + 3*pend.B*t**2 + 2*pend.C*t + pend.D
    pend.s = pend.A*abs(sin(phi))
    pend.l += dt*pend.v 
    if pend.l <= 0:
        pend.l = -pend.l
        pend.v = -pend.v
    pend.alpha += dt*pend.w

def RK_4(pend, t, dt):
    """
    Here we calculate the value of velocity and angle-velocity
    on the next iteration
    1) phi is a function of time in the argument of motor-coordinate sinus-function
    2) phi_prime is the first prime of phi function of time
    3) phi_dprime is the second prime of phi function of time
    4) v - velocity; w - angle-velocity; aplha - angle; l - length of spring
    """
    phi = pend.A4*t**4 + pend.B*t**3 + pend.C*t**2 + pend.D*t + pend.E
    phi_prime = 4*pend.A4*t**3 + 3*pend.B*t**2 + 2*pend.C*t + pend.D 
    phi_dprime = 12*pend.A4*t**2 + 6*pend.B*t + 2*pend.C
    pend.s = pend.A*abs(sin(phi))
    pend.v += dt*(-pend.mu_m*pend.v + pend.A*(sin(phi)*(phi_prime**2) - cos(phi)*phi_dprime) + pend.w**2*(pend.l + pend.s) 
    + g*cos(pend.alpha) - pend.k*(pend.l - pend.l0))
    pend.w += dt*(-pend.mu_m*pend.w - (g*sin(pend.alpha) + 2*pend.w)/(pend.l + pend.s))
