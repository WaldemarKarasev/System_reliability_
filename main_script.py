#Source code to calculate the value of P(t) and Q(t)
import numpy as np

import Functions

#Input Data
N = np.array([5, 8, 10]).reshape(1, 3)
L = np.array([1/500, 1/250]).reshape(2, 1)
print(N)
print(L)

#SERIAL CONNECTION
#summing all l[i] by n[i] time to get l_sys
l_sys = np.dot(L, N)

#using l_sys to calculate Tc for Serial connection
Tc = np.copy(np.power(l_sys, -1))

#define t for Serial and Parallen connection.  t = 3*Tc
#t is used to calculate Pc and Qc for Serial and Parralel connection
t = np.copy(np.multiply(Tc, 3))

#4 find Pc for Serial connection
Pc = np.ones(Tc.shape, dtype=float)
for i in range(Pc.shape[0]):
    for j in range(Pc.shape[1]):
        Pc[i][j] = np.exp(-l_sys[i][j]*t[i][j])

#find Qc for Serial connection
Qc = np.ones(Tc.shape, dtype=float)
for i in range(Qc.shape[0]):
    for j in range(Qc.shape[1]):
        Qc[i][j] = 1 - Pc[i][j]


#checking the sum of probabilities for Serial connection
Pc_plus_Qc = np.add(Pc, Qc)
print(Pc_plus_Qc)



#PARALLEL CONNECTION
#calculation of the integral to finding the Tcp_p  of a system with Parallel connection
#the method of rectangles was used to calculate the integral for Tcp_p
Tcp_p = np.zeros(shape=(2, 3))
for l in range(L.shape[0]):
    for n in range(N.shape[1]):
        Tcp_p[l][n]= Functions.Integral(N[0][n],L[l][0])
print(Tcp_p)

t_p = np.copy(np.multiply(Tcp_p, 3))

#find Qc_p for Parallen connection
Qc_p = np.ones(Tc.shape, dtype=float)
for i in range(Qc_p.shape[0]):
    for j in range(Qc_p.shape[1]):
        Qc_p[i][j] = np.power(1-np.exp(-l_sys[i][j]*t_p[i][j]), N[0][j])

#find Pc_p for Parallel connection
Pc_p = np.ones(Tc.shape, dtype=float)
for i in range(Pc_p.shape[0]):
    for j in range(Pc_p.shape[1]):
        Pc_p[i][j] = 1 - Qc_p[i][j]

#checking the sum of probabilities for Parallel connection
PcP_plus_QcP = np.add(Pc_p, Qc_p)
print(PcP_plus_QcP)

#create the dictionary and use it to export result of calculation to excel file
data = []
for l in range(L.shape[0]):
    for n in range(N.shape[1]):
        dict_tmp = {
        'n' : N[0][n],
        '\u03BB' : L[l][0],
        'Tc': Tc[l][n],
        't' : t[l][n],
        'Pc(t)': Pc[l][n],
        'Qc(t)': Qc[l][n],
        'Tc_p': Tcp_p[l][n],
        'Pc_p(t)': Pc_p[l][n],
        'Qc_p(t)': Qc_p[l][n]
        }
        data.append(dict_tmp)

for i in data:
    print(i, '\n')
