#!/bin/bash/

import os
import numpy as np
from matplotlib import pyplot as pl

#Create Data Caches

snrh_key=[]
inch_key=[]
strainh_data=[]
strainh_time=[]
freqh_data=[]
freqh_time=[]

snrl_key=[]
incl_key=[]
strainl_data=[]
strainl_time=[]
freql_data=[]
freql_time=[]

#Load the data which is extracted from each waveform reconstruction directory

#Extracts both the reconstruction strain and frequency as a functions of time
# and stores the data in the appropriate data cache to be used for the plots.

for a in os.listdir(os.getcwd()):
    if 'inc_0' in a or 'inc_45' in a or 'inc_90' in a or 'inc_135' in a:
        for b in os.listdir(os.getcwd()+'/'+str(a)):
            if 'inc_0_snr' in b and '.ini' not in b or 'inc_45_snr' in b and '.ini' not in b or 'inc_90_snr' in b and '.ini' not in b or 'inc_135_snr' in b and '.ini' not in b:
                for c in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)):
                    if 'bayeswave_1150569652' in c:
                        for d in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)):
                            if 'post' in d and 'bay' not in d:
                                for e in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)):
                                    #Reconstruction strain data for Hanford detector
                                    if 'signal_median_time_domain_waveform.dat.0' in e:
                                        raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        strainh_data.append(raw_data_h[:,1])
                                        strainh_time.append(raw_data_h[:,0])
                                        if 'inc_0' in a:
                                            if 'snr_10' in b:
                                                snrh_key.append(10)
                                                inch_key.append(0)
                                                print 10,0
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(0)
                                                print 20,0
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(0)
                                                print 30,0
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
                                                print 10,45
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(45)
                                                print 20,45
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(45)
                                                print 30,45
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
                                                print 10,90
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(90)
                                                print 20,90
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(90)
                                                print 30,90
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
                                                print 10,90
                                            elif 'snr_20' in b:
                                                snrh_key.append(20)
                                                inch_key.append(135)
                                                print 20,90
                                            elif 'snr_30' in b:
                                                snrh_key.append(30)
                                                inch_key.append(135)
                                                print 30,90
                                            elif 'snr_40' in b:
                                                snrh_key.append(40)
                                                inch_key.append(135)
                                            elif 'snr_50' in b:
                                                snrh_key.append(50)
                                                inch_key.append(135)
                                    #Reconstruction frequency data for Hanford detector
                                    elif 'signal_median_tf.dat.0' in e:
                                        raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        freqh_data.append(raw_data_h[:,1])
                                        freqh_time.append(raw_data_h[:,0])
                                    #Reconstruction strain data for Livingston detector
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
                                                incl_key.append(135
                                            elif 'snr_30' in b:
                                                snrl_key.append(30)
                                                incl_key.append(135)
                                            elif 'snr_40' in b:
                                                snrl_key.append(40)
                                                incl_key.append(135)
                                            elif 'snr_50' in b:
                                                snrl_key.append(50)
                                                incl_key.append(135)
                                    #Reconstruction frequency data for Livingston detector
                                    elif 'signal_median_tf.dat.1' in e:
                                        raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                        freql_data.append(raw_data_l[:,1])
                                        freql_time.append(raw_data_l[:,0])

#Plot strain and frequency
#The plots have the strain and frequency as functions of time in separate subplots

#Plot for Hanford detector data
for f in range(len(strainh_data)):
    fh,(ax1,ax2)=pl.subplots(2, sharex=True)
    ax1.plot(strainh_time[f],strainh_data[f])
    ax2.plot(freqh_time[f],freqh_data[f])
    ax1.set_title('Hanford Strain and Frequency data for q_1_inc_'+str(inch_key[f])+'_snr_'+str(snrh_key[f]))
    fh.subplots_adjust(hspace=0)
    ax1.set_ylabel('Strain')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Time')
    ax1.set_xlim([1.5,2.5])
    ax2.set_xlim([1.5,2.5])
    pl.show()
    pl.close()

#Plot for Livingston detector data
for g in range(len(strainl_data)):
    fl,(ax1,ax2)=pl.subplots(2, sharex=True)
    ax1.plot(strainl_time[g],strainl_data[g])
    ax2.plot(freql_time[g],freql_data[g])
    ax1.set_title('Livingston Strain and Frequency data for q_1_inc_'+str(inch_key[g])+'_snr_'+str(snrh_key[g]))
    fl.subplots_adjust(hspace=0)
    ax1.set_ylabel('Strain')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Time')
    ax1.set_xlim([1.5,2.5])
    ax2.set_xlim([1.5,2.5])
    pl.show()
    pl.close()






