#systems of differential equations
#ode is deterministic & continuous
#for dx/dt = f(x, t)

#delta x = f * delta t - discretisation
# das ist euler methode langsamste methode
#riemann summe ist gleiches

#runge kutta is euler and trapeze

#python has multistep methods too adams

#solver needs time grid - times for solutions although these are just bits of a solution
#and method for next point

#adaptive step size control - bigger steps if possible
#stiff systems kill adaptive step size
#-> backwards differentiation formulas solves stiff systems, implicit, linear multistep
#python chooses right solver

#define starting values and startingvalue vector

import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 1. initial conditions
S0 = 500                    # initial population
Z0 = 0                      # initial zombie population
R0 = 0                      # initial death population
y0 = [S0, Z0, R0]           # initial condition vector

# 2. parameter values
P = 0       # birth rate
d = 0.0001  # 'natural' death percent (per day)
B = 0.005  # transmission percent  (per day)
G = 0.001  # resurect percent (per day)
A = 0.002   # destroy percent  (per day)

# 3. simulation time
start = 0.0  # days
end = 25      # days
number_time_points = 1500
t  = np.linspace(start, end, number_time_points)  # time grid, 1000 steps or data points

# function 'f' to solve the system dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Zi = y[1]
    Ri = y[2]
    # the model equations (see Munz et al. 2009)
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi + G*Ri - A*Si*Zi
    f2 = d*Si + A*Si*Zi - G*Ri
    return [f0, f1, f2]

# zombie apocalypse modeling

# solve the DEs
result = odeint(f, y0, t)
S = result[:, 0]
Z = result[:, 1]
R = result[:, 2]

# plot results
plt.figure()
plt.plot(t, S, label='Humans')
plt.plot(t, Z, label='Zombies')
plt.plot(t, R, label='Dead Humans')
plt.xlabel('Days from outbreak')
plt.ylabel('Population')
plt.title('Zombie Apocalypse - No Init. Dead Pop.; No New Births.')
plt.ylim([0,500])
plt.legend(loc=0)
plt.show()