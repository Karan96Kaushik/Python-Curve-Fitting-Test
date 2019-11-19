import numpy as np
import matplotlib.pyplot as plt
import sys
import math 

from scipy import optimize

print(sys.argv)

my_data = np.genfromtxt(sys.argv[1], delimiter=',') 
# Col 7:Raw_Cap 
# Col 11:Raw_Freq

#print(my_data)

humidity_data = my_data[0:,3] # Independant # Vaisala
temp_data = my_data[0:,4] # Independant # Vaisala

sgs_freq_data = my_data[0:,7]
sgs2_freq_data = my_data[0:,11]

sgs_temp_data = my_data[0:,6]
sgs2_temp_data = my_data[0:,10]

"""
y_data = my_data[0:,11] # Dependant
y_data2 = my_data[0:,7] # Dependant
#print(y_data2)
Temp_data = my_data[0:,4] # Dependant
y_data2calc = [] #-(math.sqrt(16777216000000000/(y_data2[0:2]))) #(((pow(2, 24) / (my_data[0:,11])) * 10000000) / my_data[0:,11])*100 # Dependant
for x in y_data2:
    y_data2calc.append((math.sqrt(16777216000000000/x)))
#print(humidity_data)
#print(y_data)
"""

temp_25_data = []


def PolyModel(x, a, b, c):
    return a + (b*x) + (c*x*x)

def LinModel(x, m, c):
    return (m*x)+c


paramsLin, params_covarianceLin = optimize.curve_fit(LinModel, humidity_data, y_data2calc)
paramsPoly, params_covariancePoly = optimize.curve_fit(PolyModel, humidity_data, y_data)

print(paramsLin)
print(paramsPoly)

plt.figure(figsize=(6, 4))
#plt.scatter(humidity_data, y_data2calc, label='Data')
#plt.plot(humidity_data, y_data2calc, label='DataCalc')
#plt.scatter(humidity_data, y_data2, label='Data 2')
#plt.plot(humidity_data, PolyModel(humidity_data, paramsPoly[0], paramsPoly[1],paramsPoly[2]),label='Poly Fitted function')
plt.plot(humidity_data, LinModel(humidity_data, paramsLin[0], paramsLin[1]),label='Linear Fitted function')
#plt.plot(humidity_data, LinModel(humidity_data, -194, 543281),label='Linear Test function')
#plt.plot(humidity_data, LinModel(humidity_data,-1.76905630e+02, 5.40547063e+05),label='1 Fitted function')
#plt.plot(humidity_data, LinModel(humidity_data,-1.94096607e+02, 5.43316722e+05),label='2 Fitted function')
#plt.plot(humidity_data, LinModel(humidity_data,-1.76882431e+02, 5.41493803e+05),label='3 Fitted function')
#plt.plot(humidity_data, LinModel(humidity_data,-1.76800537e+02, 5.42334420e+05),label='4 Fitted function')
#plt.plot(humidity_data, LinModel(humidity_data,-1.71690297e+02, 5.41306424e+05),label='5 Fitted function')

plt.legend(loc='best')

plt.show()