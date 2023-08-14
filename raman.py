def main():
    no = 0 #Número de stokes a calcular

    wl = [1.06, 1.12, 1.18, 1.24, 1.30] #Longitud de onda expresada en micrómetros
    wl_m = wl_convertion(wl) #Longitud de onda expresada en metros

    ac = [0.85, 0.7, 0.6, 0.5, 0.48] #Coeficiente de atenuación de la fibra en dB/km
    ac_m = [] #Coeficiente de atenuación de la fibra en m^-1 

    raman_gain(wl)
    print()
    

def raman_gain(wl):
    rg = []
    print('Your system has the folowing Raman Gains (mW^-1): ')
    for i in wl:
        rg.append( (1.064 / i) * 9.2E-14)

    for i in range(len(rg)):
        print(str(i) + ".-" + "\t\t{:.16f}".format(rg[i]) + "\t = \t" + str(rg[i]) )

def wl_convertion(wl):
    print('Your system has the folowing wavelenghts (m): ')
    wl_m = []
    for i in wl:
        wl_m.append(i * 1E-7)

    for i in range(len(wl_m)):
        print(str(i) + ".-" + "\t\t{:.10f}".format(wl_m[i]))

    print()
    return wl_m

if __name__ == "__main__":
    main()

