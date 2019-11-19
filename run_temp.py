import numpy as np
import matplotlib.pyplot as plt
import sys
import math 
from scipy import optimize

#print(sys.argv)

my_data = np.genfromtxt(sys.argv[1], delimiter=',') 

humidity_data = my_data[0:,3]   # Independant # Vaisala
temp_data = my_data[0:,4]       # Independant # Vaisala
sgs_freq_data = my_data[0:,7]
sgs2_freq_data = my_data[0:,11]
sgs_temp_data = my_data[0:,6]
sgs2_temp_data = my_data[0:,10]



indep_data = humidity_data
dep_data = sgs_freq_data

def get_temp_std_data(test_temp_val):
    temp_std_data_freq_arr = []
    temp_std_data_hum_arr = []

    i=-1
    for x in dep_data:
        i = i + 1
        if abs(sgs_temp_data[i]-test_temp_val) < 1.5:
            temp_std_data_freq_arr.append(x)
            temp_std_data_hum_arr.append(indep_data[i])

    return temp_std_data_freq_arr,temp_std_data_hum_arr

def get_lin(indep,dep):
    paramsLin, params_covarianceLin = optimize.curve_fit(LinModel, indep, dep)
    #print(paramsLin)
    return paramsLin

def LinModel(x, m, c):
	return (m*x)+c


#dep,indep = 

temp_dep_m_c = []

temp_list = [10,25,35,39]

for temp in temp_list:
    a = get_lin(get_temp_std_data(temp)[1], get_temp_std_data(temp)[0])
    b = [a[0],a[1],temp]

    temp_dep_m_c.append(b)
    print(str(temp) + " : " + str(get_lin(get_temp_std_data(temp)[1],get_temp_std_data(temp)[0])))

print(temp_dep_m_c)

#print(temp_dep_m_c[1][0:])

temps = []
Ms = []
Cs = []

for val in temp_dep_m_c:
    temps.append(val[2])
    Ms.append(val[0])
    Cs.append(val[1])

print("M : " + str(get_lin(temps,Ms)))
print("C : " + str(get_lin(temps,Cs)))


"""
    Hum = Freq - C
          ---------
              M

    M = m1.x + c1
    C = m2.x + c2
"""
