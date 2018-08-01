import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

R0 = 300 #rabbit start value
F0 = 10 #fox start value
y0 = [R0, F0] # initial state vector

#Parameters

p = [a, b, c, d]

p = [1, 1, 1, 1]

def f(y, p, t):

	R = y
	dR = a*R - b*R*F
	dF = d * b* R*F - c * F
	return (dR, dF)

