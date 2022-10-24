import numpy as np

#function for numerical calculation of the integral
def Integral(n, l):
    t = np.arange(1, 100000, 0.005, dtype=float)
    Tc_p = 0
    for i in range(1, t.size):
        Pc = (1 - np.power(1 - np.exp(-l * ((t[i-1] + t[i])/2)), n))
        Tc_p_tmp = Pc * (t[i] - t[i - 1])
        Tc_p += Tc_p_tmp
        if Pc < 0.003:
            return Tc_p
    return Tc_p



#function for Setting collor and style for plot
def Select_Color_and_Stile(IndexList):
    color_and_style_dict = {
        (0, 0): 'r-',
        (0, 1): 'b-',
        (0, 2): 'g-',
        (1, 0): 'r:',
        (1, 1): 'b:',
        (1, 2): 'g:',
    }

    if len(IndexList) > 2:
        print('wrong index input\nuse array with shape(2,)\n')
        return 'w'

    for key, value in color_and_style_dict.items():
        if tuple(IndexList) == key:
            return value

    return 'w'