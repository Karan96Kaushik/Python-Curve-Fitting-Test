import numpy as np
import matplotlib.pyplot as plt
import sys
import math 

from scipy import optimize

test_temp = 39

print(sys.argv)

my_data = np.genfromtxt(sys.argv[1], delimiter=',') 

humidity_data = my_data[0:,3] # Independant # Vaisala
temp_data = my_data[0:,4] # Independant # Vaisala

sgs_freq_data = my_data[0:,7]
sgs2_freq_data = my_data[0:,11]

sgs_temp_data = my_data[0:,6]
sgs2_temp_data = my_data[0:,10]

func_data = []

temp_std_data_freq = []
temp_std_data_hum = []

i=-1
for x in sgs_freq_data:
	i = i + 1
	if abs(sgs_temp_data[i]-test_temp) < 1.5:
		temp_std_data_freq.append(x)
		temp_std_data_hum.append(humidity_data[i])
	
def PolyModel(x, a, b, c):
	return a + (b*x) + (c*x*x)

def LinModel(x, m, c):
	return (m*x)+c

indep_data = temp_std_data_hum
dep_data = temp_std_data_freq

paramsLin, params_covarianceLin = optimize.curve_fit(LinModel, indep_data, dep_data)
paramsPoly, params_covariancePoly = optimize.curve_fit(PolyModel, indep_data, dep_data)

print(paramsLin)
print(paramsPoly)

plt.figure(figsize=(6, 4))
#plt.scatter(indep_data, dep_data, label='Data')

paramsA = [-4.37571303e+01, 5.50682781e+05]
paramsB = [-6.49137947e+01, 5.48753740e+05]
paramsC = [-7.10032280e+01, 5.47593916e+05]
paramsD = [-7.52340530e+01, 5.46819329e+05]

func_dataA = []
func_dataB = []
func_dataC = []
func_dataD = []

for x in indep_data:
	func_dataA.append(LinModel(x, paramsA[0], paramsA[1]))

for x in indep_data:
	func_dataB.append(LinModel(x, paramsB[0], paramsB[1]))

for x in indep_data:
	func_dataC.append(LinModel(x, paramsC[0], paramsC[1]))

for x in indep_data:
	func_dataD.append(LinModel(x, paramsD[0], paramsD[1]))

#paramsA = [[-4.37571303e+01, 5.50682781e+05],]
plt.plot(indep_data, func_dataA,label='Linear Fitted function')
plt.plot(indep_data, func_dataB,label='Linear Fitted function')
plt.plot(indep_data, func_dataC,label='Linear Fitted function')
plt.plot(indep_data, func_dataD,label='Linear Fitted function')

plt.legend(loc='best')

plt.show()