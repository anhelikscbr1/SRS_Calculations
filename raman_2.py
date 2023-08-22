import math as mt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.integrate import odeint
figure(dpi=400)

def main():
    time_frec()


def odes(v,z):
    na = 0.2 #Apertura numérica de la fibra óptica NA
    a_n = 4.5 #Radio del núcleo de la fibra en micrómetros
    wl = [1.06, 1.12, 1.18, 1.24, 1.30] #Longitud de onda expresada en micrómetros
    ac = [0.85, 0.7, 0.6, 0.5, 0.48] #Coeficiente de atenuación de la fibra en dB/km
    wl_m = []
    rg = []
    for i in wl:
        wl_m.append(i * 1E-6)
    ac_m = []
    for i in ac:
        ac_m.append ((i / 4.343) * 1E-3)
    for i in wl:
        rg.append( (1.064 / i) * 9.2E-14)
    normalizedFrecuency = []
    effArea = []
    a_n = a_n*1E-6 #Radio de la fibra en metros
    for i in  wl_m:
        n_frec = ( 2 * np.pi * na * a_n  / i)
        normalizedFrecuency.append( n_frec)
    
    for i in normalizedFrecuency:
        eff_a = np.pi * ( a_n * ( 0.65 + ( 1.619 / i ** (3/2) ) + ( 2.879 / i ** (6)))) ** (2)
        effArea.append(eff_a)
    
    x = v[0]
    y = v[1]
    a = v[2]
    b = v[3]
    c = v[4]
    
    dp_dz = (wl_m[1]/wl_m[0])*(-rg[1]/effArea[1])* y*x - ac_m[0] *x
    d1s_dz = (rg[1]/effArea[0])*y*x - (wl_m[2]/wl_m[1])*(rg[2]/effArea[2])*y*a - ac_m[1]*y
    d2s_dz = (rg[2]/effArea[1])*a*y -  (wl_m[3]/wl_m[2])*(rg[3]/effArea[3])*a*b - ac_m[2] *a 
    d3s_dz = (rg[3]/effArea[2])*a*b -  (wl_m[4]/wl_m[3])*(rg[4]/effArea[4])*b*c - ac_m[3] *b
    d4s_dz = (rg[4]/effArea[3])* b*c - ac_m[4] *c
    
    return [dp_dz, d1s_dz, d2s_dz, d3s_dz, d4s_dz]

def time_frec():

    max_power = 14
    no_points = 3000
    t = np.linspace(-30,30,no_points)
    #gaussian = max_power*mt.e ** (-(t**2)/2)
    FWHM = 10 
    #gaussian = max_power * 2 ** -((2* t / FWHM ) ** 2)
    #plt.plot(t,gaussian, 'b', label = "Gaussiano")
    sech = max_power / (np.cosh((1.7627 * t) / (FWHM))) ** 2
    gaussian = sech

    response_s = []
    response_1s = []
    response_2s = []
    response_3s = []
    response_4s = []
    exit_value = 100
    simulation_distance = 2400
    for i in range(no_points):
       
        seed = max_power * 0.0000001
        x0 = [gaussian[i], seed,seed,seed,seed]
    
        #declare a z range
        z = np.linspace(0, simulation_distance, exit_value+1)
        sol = odeint(odes, x0, z)
    
        p_z = sol [:,0]
        s1_z = sol [:,1]
        s2_z = sol [:,2]
        s3_z = sol [:,3]
        s4_z = sol [:,4]
    
        response_s.append(float(p_z[exit_value]))
        response_1s.append(float(s1_z[exit_value]))
        response_2s.append(float(s2_z[exit_value]))
        response_3s.append(float(s3_z[exit_value]))
        response_4s.append(float(s4_z[exit_value]))

    plt.plot(t,response_s, 'c', label="Fuente")
    plt.plot(t,response_1s, 'y', label="Stokes 1")
    plt.plot(t,response_2s, 'g', label="Stokes 2")
    plt.plot(t,response_3s, 'r', label="Stokes 3")
    plt.plot(t,response_4s, 'm', label="Stokes 4")
    plt.plot(t,gaussian, 'b', label = "sech^2")
    plt.xlabel("Tiempo (fs)")
    plt.ylabel("Potencia (W)")
    plt.axis([-30, 30, 0, max_power + 0.1])
    plt.legend()
    plt.show()
    return

if __name__ == "__main__":
    main()