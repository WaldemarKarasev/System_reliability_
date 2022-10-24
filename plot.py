#Source code to plot graphics for P(t) abd Q(t) using matplotlib

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator

import Functions

#Initial Data
N = np.array([5, 8, 10]).reshape(1, 3)
L = np.array([1/500, 1/250]).reshape(2, 1)
print(N)
print(L)

#SERIAL CONNECTION
#Summing all l[i] by n[i] time to get l_sys
l_sys = np.dot(L, N)

#Using l_sys to calculate Tc
Tc = np.copy(np.power(l_sys, -1))

#Define array of t equal 3*Tc for SERIAL connection
t = np.copy(np.multiply(Tc, 3))
print("t:\n", t)

#The variable to set the number of points to plot SERIAL connection
time_points = 15

ti = np.zeros(shape=(2, 3, time_points))
for i in range(t.shape[0]):
    for j in range(t.shape[1]):
        ti[i][j] = np.linspace(0, t[i][j], time_points)
print(ti.shape)

#Pc and Qc plotting 2*3 for SERIAL CONNECTION
#Calculating arrays of Pc and Qc for plotting graphics
Pc_plt = np.zeros(shape=(2, 3, time_points))
Qc_plt = np.zeros(shape=(2, 3, time_points))
P_plus_Q = np.zeros(shape=(2, 3, time_points))

for i in range(ti.shape[0]):
    for j in range(ti.shape[1]):
        Pc_plt[i][j] = np.exp(-l_sys[i][j]*ti[i][j])
        Qc_plt[i][j] = 1 - Pc_plt[i][j]
        P_plus_Q[i][j] = Pc_plt[i][j] + Qc_plt[i][j]

print(Pc_plt.shape)
print(Qc_plt.shape)
print(P_plus_Q.shape)

# 2*3 plot of Pc for SERIAL connection
for i in range(ti.shape[0]):
    for j in range(ti.shape[1]):
        plt.plot(ti[i][j], Pc_plt[i][j], Functions.Select_Color_and_Stile([i, j]))
plt.title('Вероятность работы безотказной работы P(t)\nпри последовательном соединении')
plt.xlabel('t, час')
plt.ylabel('P(t)')
plt.ylim(0, 1)
plt.xlim(0, 350)
plt.yticks(np.arange(0, 1.05, step=0.05))
plt.xticks(np.arange(0, 350, step=25))
plt.legend(['n=3, $\lambda$=1/500', 'n=5, $\lambda$=1/500', 'n=10, $\lambda$=1/500',
            'n=3, $\lambda$=1/250', 'n=5, $\lambda$=1/250', 'n=10, $\lambda$=1/250'])
plt.grid()
plt.show()

# 2*3 plot of Qc for SERIAL connection
for i in range(ti.shape[0]):
    for j in range(ti.shape[1]):
        plt.plot(ti[i][j], Qc_plt[i][j], Functions.Select_Color_and_Stile([i, j]))
plt.title('Вероятность отказа Q(t)\nпри последовательном соединении')
plt.xlabel('t, час')
plt.ylabel('Q(t)')
plt.ylim(0, 1)
plt.xlim(0, 350)
plt.yticks(np.arange(0, 1.05, step=0.05))
plt.xticks(np.arange(0, 350, step=25))
plt.legend(['n=3, $\lambda$=1/500', 'n=5, $\lambda$=1/500', 'n=10, $\lambda$=1/500',
            'n=3, $\lambda$=1/250', 'n=5, $\lambda$=1/250', 'n=10, $\lambda$=1/250'])
plt.grid()
plt.show()



#define array of t_p for PARALLEL connection
Tcp_p = np.zeros(shape=(2, 3))

#Calculating Tc_p
for l in range(L.shape[0]):
    for n in range(N.shape[1]):
        Tcp_p[l][n]= Functions.Integral(N[0][n],L[l][0])
print(Tcp_p)

#Define array of t equal 3*Tc_p for PARALLEL connection
t_p = np.copy(np.multiply(Tcp_p, 3))

#The variable to set the number of points to plot PARALLEL connection
time_points_p = 100
ti_p = np.zeros(shape=(2, 3, time_points_p))
for i in range(t_p.shape[0]):
    for j in range(t_p.shape[1]):
        ti_p[i][j] = np.linspace(0, t_p[i][j], time_points_p)
print(ti_p.shape)

#plotting 2*3 for PARALLEL CONNECTION
# calculate arrays of Pc_p and Qc_p for plotting graphics
Pc_p_plt = np.zeros(shape=(2, 3, time_points_p))
Qc_p_plt = np.zeros(shape=(2, 3, time_points_p))
Pp_plus_Qp = np.zeros(shape=(2, 3, time_points_p))

for i in range(ti_p.shape[0]):
    for j in range(ti_p.shape[1]):
        Qc_p_plt[i][j] = np.power(1-np.exp(-l_sys[i][j]*ti_p[i][j]), N[0][j])
        Pc_p_plt[i][j] = 1 - Qc_p_plt[i][j]
        Pp_plus_Qp[i][j] = Pc_p_plt[i][j] + Qc_p_plt[i][j]

print(Pc_p_plt.shape)
print(Qc_p_plt.shape)

# 2*3 plot of Pc_p for PARALLEL connection
for i in range(ti_p.shape[0]):
    for j in range(ti_p.shape[1]):
        plt.plot(ti_p[i][j], Pc_p_plt[i][j], Functions.Select_Color_and_Stile([i, j]))
plt.title('Вероятность работы безотказной работы P_p(t)\nпри параллельном соединении')
plt.xlabel('t, час')
plt.ylabel('P_p(t)')
plt.ylim(0, 1)
plt.xlim(0, 1000)
plt.yticks(np.arange(0, 1.05, step=0.05))
plt.xticks(np.arange(0, 1025, step=25))
plt.legend(['n=3, $\lambda$=1/500', 'n=5, $\lambda$=1/500', 'n=10, $\lambda$=1/500',
            'n=3, $\lambda$=1/250', 'n=5, $\lambda$=1/250', 'n=10, $\lambda$=1/250'])
plt.grid()
plt.show()

# 2*3 plot of Qc_p for PARALLEL connection
for i in range(ti_p.shape[0]):
    for j in range(ti_p.shape[1]):
        plt.plot(ti_p[i][j], Qc_p_plt[i][j], Functions.Select_Color_and_Stile([i, j]))

plt.title('Вероятность отказа Q_p(t)\nпри параллельном соединении')
plt.xlabel('t, час')
plt.ylabel('Q_p(t)')
plt.ylim(0, 1)
plt.xlim(0, 1000)
plt.yticks(np.arange(0, 1.05, step=0.05))
plt.xticks(np.arange(0, 1025, step=25))
plt.legend(['n=3, $\lambda$=1/500', 'n=5, $\lambda$=1/500', 'n=10, $\lambda$=1/500',
            'n=3, $\lambda$=1/250', 'n=5, $\lambda$=1/250', 'n=10, $\lambda$=1/250'])
plt.grid()
plt.show()