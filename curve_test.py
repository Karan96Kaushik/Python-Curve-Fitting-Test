import numpy as np
import matplotlib.pyplot as plt
import sys
import math 

from scipy import optimize

test_temp = 25

print(sys.argv)

my_data = np.genfromtxt(sys.argv[1], delimiter=',') 


def PolyModel(x, a, b, c):
	return a + (b*x) + (c*x*x)

def LinModel(x, m, c):
	return (m*x)+c

indep_data = my_data[0:,2]
dep_data = my_data[0:,0]

paramsLin, params_covarianceLin = optimize.curve_fit(LinModel, indep_data, dep_data)
paramsPoly, params_covariancePoly = optimize.curve_fit(PolyModel, indep_data, dep_data)

print(paramsLin)
print(paramsPoly)

plt.figure(figsize=(6, 4))
plt.scatter(indep_data, dep_data, label='Data')

plt.plot(indep_data, LinModel(indep_data, -1.1, paramsLin[1]),label='Linear Fitted function')
plt.plot(indep_data, LinModel(indep_data, paramsLin[0], paramsLin[1]),label='Linear Fitted function')

plt.legend(loc='best')

plt.show()