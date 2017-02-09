#!/bin/bash/

import os
import numpy as np
from matplotlib import pyplot as pl

#Create data caches

snrh_key=[]
inch_key=[]
strainh_data=[]
strainh_time=[]
injectsh_data=[]
h_time=[]

snrl_key=[]
incl_key=[]
strainl_data=[]
strainl_time=[]
injectsl_data=[]
l_time=[]

#Load the data from reconstruction and injection waveform directory files
for a in os.listdir(os.getcwd()):
    if 'inc_0' in a or 'inc_45' in a or 'inc_90' in a or 'inc_135':
        for b in os.listdir(os.getcwd()+'/'+str(a)):
            if 'inc_0_snr' in b and '.ini' not in b or 'inc_45_snr' in b and '.ini' not in b or 'inc_90_snr' in b and '.ini' not in b or 'inc_135_snr' in b and '.ini' not in b:
                for c in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)):
                    if 'bayeswave_1150569652' in c:
                        for d in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)):
                            if 'post' in d and 'bay' not in d:
                                for e in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)):
                                    #Reconstruction strain data as a function of time for Hanford detector
                                    if 'signal_median_time_domain_waveform.dat.0' in e:
                                        raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        strainh_data.append(raw_data_h[:,1])
                                        strainh_time.append(raw_data_h[:,0])
                                        if 'inc_0' in a:
                                            if 'snr_10' in b:
                                                snrh_key.append(10)
                                                inch_key.append(0)
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(0)
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(0)
                                            elif 'snr_40' in b:
                                                snrh_key.append(40)
                                                inch_key.append(0)
                                            elif 'snr_50' in b:
                                                snrh_key.append(50)
                                                inch_key.append(0)
                                        elif 'inc_45' in a:
                                            if 'snr_10' in b:
                                                snrh_key.append(10)
                                                inch_key.append(45)
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(45)
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(45)
                                            elif 'snr_40' in b:
                                                snrh_key.append(40)
                                                inch_key.append(45)
                                            elif 'snr_50' in b:
                                                snrh_key.append(50)
                                                inch_key.append(45)
                                        elif 'inc_90' in a:
                                            if 'snr_10' in b:
                                                snrh_key.append(10)
                                                inch_key.append(90)
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(90)
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(90)
                                            elif 'snr_40' in b:
                                                snrh_key.append(40)
                                                inch_key.append(90)
                                            elif 'snr_50' in b:
                                                snrh_key.append(50)
                                                inch_key.append(90)
                                        elif 'inc_135' in a:
                                            if 'snr_10' in b:
                                                snrh_key.append(10)
                                                inch_key.append(135)
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(135)
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(135)
                                            elif 'snr_40' in b:
                                                snrh_key.append(40)
                                                inch_key.append(135)
                                            elif 'snr_50' in b:
                                                snrh_key.append(50)
                                                inch_key.append(135)
                                    #Injection strain data as a function of time for Hanford detector
                                    elif 'injected_whitened_waveform.dat.0' in e:
                                        raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        injectsh_data.append(raw_data_h)
                                    #Reconstruction strain data as a function of time for Livingston detector
                                    elif 'signal_median_time_domain_waveform.dat.1' in e:
                                        raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        strainl_data.append(raw_data_l[:,1])
                                        strainl_time.append(raw_data_l[:,0])
                                        if 'inc_0' in a:
                                            if 'snr_10' in b:
                                                snrl_key.append(10)
                                                incl_key.append(0)
                                            elif 'snr_20' in b:
                                                snrl_key.append(20)
                                                incl_key.append(0)
                                            elif 'snr_30' in b:
                                                snrl_key.append(30)
                                                incl_key.append(0)
                                            elif 'snr_40' in b:
                                                snrl_key.append(40)
                                                incl_key.append(0)
                                            elif 'snr_50' in b:
                                                snrl_key.append(50)
                                                incl_key.append(0)
                                        elif 'inc_45' in a:
                                            if 'snr_10' in b:
                                                snrl_key.append(10)
                                                incl_key.append(45)
                                            elif 'snr_20' in b:
                                                snrl_key.append(20)
                                                incl_key.append(45)
                                            elif 'snr_30' in b:
                                                snrl_key.append(30)
                                                incl_key.append(45)
                                            elif 'snr_40' in b:
                                                snrl_key.append(40)
                                                incl_key.append(45)
                                            elif 'snr_50' in b:
                                                snrl_key.append(50)
                                                incl_key.append(45)
                                        elif 'inc_90' in a:
                                            if 'snr_10' in b:
                                                snrl_key.append(10)
                                                incl_key.append(90)
                                            elif 'snr_20' in b:
                                                snrl_key.append(20)
                                                incl_key.append(90)
                                            elif 'snr_30' in b:
                                                snrl_key.append(30)
                                                incl_key.append(90)
                                            elif 'snr_40' in b:
                                                snrl_key.append(40)
                                                incl_key.append(90)
                                            elif 'snr_50' in b:
                                                snrl_key.append(50)
                                                incl_key.append(90)
                                        elif 'inc_135' in a:
                                            if 'snr_10' in b:
                                                snrl_key.append(10)
                                                incl_key.append(135)
                                            elif 'snr_20' in b:
                                                snrl_key.append(20)
                                                incl_key.append(135)
                                            elif 'snr_30' in b:
                                                snrl_key.append(30)
                                                incl_key.append(135)
                                            elif 'snr_40' in b:
                                                snrl_key.append(40)
                                                incl_key.append(135)
                                            elif 'snr_50' in b:
                                                snrl_key.append(50)
                                                incl_key.append(135)
                                    #Injection strain data as a function of time for Livingston detector
                                    elif 'injected_whitened_waveform.dat.1' in e:
                                        raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        injectsl_data.append(raw_data_l)


#Plot residual strain of waveform which is obtained from
# subtracting the injection strain data from the
# reconstruction strain data.

#Plot the residual strain data for the Hanford detector
for f in range(len(strainh_data)):
    fh,ax=pl.subplots()
    ax.plot(strainh_time[f],strainh_data[f]-injectsh_data[f])
    ax.set_title('Hanford Residual Strain data for q_1_inc_'+str(inch_key[f])+'_snr_'+str(snrh_key[f]))
    ax.set_ylabel('Residual Strain')
    ax.set_xlabel('Time')
    ax.set_xlim([0,2.5])
    pl.show()
    pl.close()

#Plot the residual straing data for the Livingston detector
for g in range(len(strainl_data)):
    fl,ax=pl.subplots()
    ax.plot(strainl_time[g],strainl_data[g]-injectsl_data[g])
    ax.set_title('Livingston Residual Strain data for q_1_inc_'+str(incl_key[g])+'_snr_'+str(snrl_key[g]))
    ax.set_ylabel('Residual Strain')
    ax.set_xlabel('Time')
    ax.set_xlim([0,2.5])
    pl.show()
    pl.close()






