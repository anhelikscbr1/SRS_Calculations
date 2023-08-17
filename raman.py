import numpy as np

def main():
    na = 0.2 #Apertura numérica de la fibra óptica NA
    a = 6 #Radio del núcleo de la fibra en micrómetros

    wl = [1.06, 1.12, 1.18, 1.24, 1.30] #Longitud de onda expresada en micrómetros
    wl_m = wl_convertion(wl) #Longitud de onda expresada en metros

    ac = [0.85, 0.7, 0.6, 0.5, 0.48] #Coeficiente de atenuación de la fibra en dB/km
    ac_m = ac_convertion(ac) #Coeficiente de atenuación de la fibra en m^-1 

    rg = raman_gain(wl)
    eff_a = effecive_area(na, a, wl_m)
    raman_threshold(eff_a, ac_m, rg)
 

def raman_gain(wl):
    rg = []
    print('Your system has the folowing Raman Gains (mW^-1): ')
    for i in wl:
        rg.append( (1.064 / i) * 9.2E-14)

    for i in range(len(rg)):
        print(str(i) + ".-" + "\t\t{:.16f}".format(rg[i]) + "\t = \t" + str(rg[i]) )
    return rg

def wl_convertion(wl):
    print('Your system has the folowing wavelenghts (m): ')
    wl_m = []
    for i in wl:
        wl_m.append(i * 1E-6)

    for i in range(len(wl_m)):
        print(str(i) + ".-" + "\t\t{:.10f}".format(wl_m[i]))

    print()
    return wl_m

def ac_convertion(ac):
    print('Your system has the folowing atenuation coeficients (m^-1): ')
    ac_m = []
    for i in ac:
        ac_m.append ((i / 4.343) * 1E-3)
    for i in range(len(ac_m)):
        print(str(i) + ".-" + "\t\t{:.6f}".format(ac_m[i]))
    return ac_m

def effecive_area(na, a, wl_m):
    print('The effective area is: ')
    normalizedFrecuency = []
    effectiveArea = []
    a = a*1E-6 #Radio de la fibra en metros
    for i in  wl_m:
        n_frec = ( 2 * np.pi * na * a  / i)
        normalizedFrecuency.append( n_frec)
    
    for i in normalizedFrecuency:
        eff_a = np.pi * ( a * ( 0.65 + ( 1.619 / i ** (3/2) ) + ( 2.879 / i ** (6)))) ** (2)
        effectiveArea.append(eff_a)
    print(effectiveArea)
    return effectiveArea

def raman_threshold(eff_a, ac_m, rg):
    print('Raman threshold (W): ')
    print()
    raman_tsh = []
    for i in range(len(rg)):
        raman_tsh.append(16 * ac_m[i] * eff_a[i] / rg[i])
    print(raman_tsh)

if __name__ == "__main__":
    main()