# Modeling-of-fluctuations
Repository for our team's project

Task is to create a visualisation of fluctuations, basing on the start-up conditions.

Input consists of several variables: 
1) l0 - length of spring without deformation (=const)
2) l - length of spring at the moment. l may be changed. Initially l = start-up length of the spring
3) k - asperity of spring
4) A - amplitude of motor fluctuations
5) s - coordinate of the motor at the moment
6) alpha - the deflection angle. Initially alpha = alpha0 - the start-up angle
7) v - speed of body along the rod. Initially v = v0 - start-up speed
8) w - angular speed of body. Initially w = w0 - start-up angular speed
9) mu/m - ratio coefficient of friction to mass
10) A4 - coefficient at t^4
11) B - coefficient at t^3
12) C - coefficient at t^2
13) D - coefficient at t
14) E - free member. It specifies start-up coordinate of the motor
fi is function of time. fi specifies phase change of motor. fi is polynomial of degree 4. fi = A_4t^4 + Bt^3 + Ct^2 + Dt + E 
Spring is unloaded in t = 0.

Note: to launch the code correctly, check the path to file input.txt in File_with_functions.py.
