#!/bin/bash/

import os
import numpy as np
from matplotlib import pyplot as pl

#Create Data Caches

qh_key=[]
snrh_key=[]
inch_key=[]
strainh_data=[]
strainh_time=[]
injecth_data=[]
freqh_data=[]
freqh_time=[]
inject_freqh_data=[]
reconstructions_hdata=[]

ql_key=[]
snrl_key=[]
incl_key=[]
strainl_data=[]
strainl_time=[]
injectl_data=[]
freql_data=[]
freql_time=[]
inject_freql_data=[]
reconstructions_ldata=[]

#Load the data which is extracted from each waveform reconstruction directory

#Extracts both the reconstruction strain and frequency as a functions of time
# and stores the data in the appropriate data cache to be used for the plots.

for a in os.listdir(os.getcwd()):
    if 'q_1' in a or 'q_5' in a:
        for b in os.listdir(os.getcwd()+'/'+str(a)):
            if 'inc_0' in b or 'inc_45' in b or 'inc_90' in b or 'inc_135' in b or 'inc_180' in b or 'inc_225' in b or 'inc_270' in b or 'inc_315' in b or 'inc_360' in b:
                print b
                for c in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)):
                    if 'inc_0_snr' in c and '.ini' not in c or 'inc_45_snr' in c and '.ini' not in c or 'inc_90_snr' in c and '.ini' not in c or 'inc_135_snr' in c and '.ini' not in c or 'inc_180_snr' in c and '.ini' not in c or 'inc_225_snr' in c and '.ini' not in c or 'inc_270_snr' in c and '.ini' not in c or 'inc_315_snr' in c and '.ini' not in c or 'inc_360_snr' in c and '.ini' not in c:
                        for d in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)):
                            if 'bayeswave_1150569652' in d:
                                for e in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)):
                                    if 'post' in e and 'bay' not in e:
                                        for f in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)):
                                            #Reconstruction strain data for Hanford detector
                                            if 'signal_median_time_domain_waveform.dat.0' in f:
                                                raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                strainh_data.append(raw_data_h[:,1])
                                                strainh_time.append(raw_data_h[:,0])
                                                if 'q_1' in a:
                                                    if 'inc_0' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(0)
                                                            print 10,0
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(0)
                                                            print 20,0
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(0)
                                                            print 30,0
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(0)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(0)
                                                    elif 'inc_45' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(45)
                                                            print 10,45
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(45)
                                                            print 20,45
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(45)
                                                            print 30,45
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(45)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(45)
                                                    elif 'inc_90' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(90)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(90)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(90)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(90)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(90)
                                                    elif 'inc_135' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(135)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(135)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(135)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(135)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(135)
                                                    elif 'inc_180' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(180)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(180)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(180)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(180)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(180)
                                                    elif 'inc_225' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(225)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(225)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(225)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(225)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(225)
                                                    elif 'inc_270' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(270)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(270)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(270)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(270)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(270)
                                                    elif 'inc_315' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(315)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(315)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(315)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(315)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(315)
                                                    elif 'inc_360' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(10)
                                                            inch_key.append(360)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(20)
                                                            inch_key.append(360)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(30)
                                                            inch_key.append(360)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(40)
                                                            inch_key.append(360)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(1)
                                                            snrh_key.append(50)
                                                            inch_key.append(360)
                                                elif 'q_5' in a:
                                                    if 'inc_0' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(0)
                                                            print 10,0
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(0)
                                                            print 20,0
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(0)
                                                            print 30,0
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(0)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(0)
                                                    elif 'inc_45' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(45)
                                                            print 10,45
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(45)
                                                            print 20,45
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(45)
                                                            print 30,45
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(45)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(45)
                                                    elif 'inc_90' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(90)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(90)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(90)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(90)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(90)
                                                    elif 'inc_135' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(135)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(135)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(135)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(135)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(135)
                                                    elif 'inc_180' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(180)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(180)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(180)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(180)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(180)
                                                    elif 'inc_225' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(225)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(225)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(225)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(225)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(225)
                                                    elif 'inc_270' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(270)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(270)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(270)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(270)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(270)
                                                    elif 'inc_315' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(315)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(315)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(315)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(315)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(315)
                                                    elif 'inc_360' in b:
                                                        if 'snr_10' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(10)
                                                            inch_key.append(360)
                                                            print 10,90
                                                        elif 'snr_20' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(20)
                                                            inch_key.append(360)
                                                            print 20,90
                                                        elif 'snr_30' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(30)
                                                            inch_key.append(360)
                                                            print 30,90
                                                        elif 'snr_40' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(40)
                                                            inch_key.append(360)
                                                        elif 'snr_50' in c:
                                                            qh_key.append(5)
                                                            snrh_key.append(50)
                                                            inch_key.append(360)
                                            #Injection strain data for Hanford detector
                                            elif 'injected_whitened_waveform.dat.0' in f:
                                                raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                injecth_data.append(raw_data_h) 
                                            #Reconstruction frequency data for Hanford detector
                                            elif 'signal_median_tf.dat.0' in f:
                                                raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                freqh_data.append(raw_data_h[:,1])
                                                freqh_time.append(raw_data_h[:,0])
                                            #Injection frequency data for Hanford detector
                                            elif 'injected_median_tf.dat.0' in f:
                                                raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                inject_freqh_data.append(raw_data_h)
                                            #Other signal reconstruction data for Hanford detector
                                            elif 'signal_recovered_whitened_waveform.dat.0' in f:
                                                raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                reconstructions_hdata.append(raw_data_h)
                                            #Reconstruction strain data for Livingston detector
                                            elif 'signal_median_time_domain_waveform.dat.1' in f:
                                                raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                strainl_data.append(raw_data_l[:,1])
                                                strainl_time.append(raw_data_l[:,0])
                                                if 'q_1' in a:
                                                    if 'inc_0' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(0)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(0)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(0)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(0)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(0)
                                                    elif 'inc_45' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(45)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(45)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(45)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(45)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(45)
                                                    elif 'inc_90' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(90)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(90)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(90)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(90)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(90)
                                                    elif 'inc_135' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(135)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(135)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(135)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(135)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(135)
                                                    elif 'inc_180' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(180)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(180)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(180)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(180)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(180)
                                                    elif 'inc_225' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(225)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(225)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(225)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(225)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(225)
                                                    elif 'inc_270' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(270)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(270)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(270)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(270)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(270)
                                                    elif 'inc_315' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(315)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(315)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(315)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(315)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(315)
                                                    elif 'inc_360' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(10)
                                                            incl_key.append(360)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(20)
                                                            incl_key.append(360)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(30)
                                                            incl_key.append(360)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(40)
                                                            incl_key.append(360)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(1)
                                                            snrl_key.append(50)
                                                            incl_key.append(360)
                                                if 'q_5' in a:
                                                    if 'inc_0' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(0)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(0)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(0)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(0)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(0)
                                                    elif 'inc_45' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(45)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(45)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(45)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(45)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(45)
                                                    elif 'inc_90' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(90)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(90)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(90)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(90)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(90)
                                                    elif 'inc_135' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(135)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(135)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(135)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(135)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(135)
                                                    elif 'inc_180' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(180)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(180)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(180)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(180)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(180)
                                                    elif 'inc_225' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(225)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(225)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(225)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(225)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(225)
                                                    elif 'inc_270' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(270)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(270)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(270)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(270)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(270)
                                                    elif 'inc_315' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(315)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(315)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(315)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(315)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(315)
                                                    elif 'inc_360' in b:
                                                        if 'snr_10' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(10)
                                                            incl_key.append(360)
                                                        elif 'snr_20' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(20)
                                                            incl_key.append(360)
                                                        elif 'snr_30' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(30)
                                                            incl_key.append(360)
                                                        elif 'snr_40' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(40)
                                                            incl_key.append(360)
                                                        elif 'snr_50' in c:
                                                            ql_key.append(5)
                                                            snrl_key.append(50)
                                                            incl_key.append(360)
                                            #Injection strain data for Livingston detector
                                            elif 'injected_whitened_waveform.dat.1' in f:
                                                raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                injectl_data.append(raw_data_l) 
                                            #Reconstruction frequency data for Livingston detector
                                            elif 'signal_median_tf.dat.1' in f:
                                                raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                freql_data.append(raw_data_l[:,1])
                                                freql_time.append(raw_data_l[:,0])
                                            #Injection frequency data for Livingston detector
                                            elif 'injected_median_tf.dat.1' in f:
                                                raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                inject_freql_data.append(raw_data_l)
                                            #Other signal reconstruction data for Livingston detector
                                            elif 'signal_recovered_whitened_waveform.dat.1' in f:
                                                raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e)+'/'+str(f))
                                                reconstructions_ldata.append(raw_data_l)

#Plot strain and frequency
#The plots have the strain and frequency as functions of time in separate subplots

#Window Size 1 (t=1.8-2.1)

#Strain/Frequency Plot for Hanford detector data
for i in range(len(strainh_data)):
    fh,(ax1,ax2)=pl.subplots(2, sharex=True)
    ax1.plot(strainh_time[i],strainh_data[i],color='r',label='Reconstruction')
    ax1.plot(strainh_time[i],injecth_data[i],color='b',label='Injection')
    ax1.legend(loc=2,fontsize='x-small')
    ax2.plot(freqh_time[i],freqh_data[i],color='r',label='Reconstruction')
    ax2.plot(freqh_time[i],inject_freqh_data[i],color='b',label='Injection')
    ax2.legend(loc=2,fontsize='x-small')
    ax1.set_title('Hanford Strain and Frequency data for q_'+str(qh_key[i])+'_inc_'+str(inch_key[i])+'_snr_'+str(snrh_key[i]))
    fh.subplots_adjust(hspace=0)
    ax1.set_ylabel('Strain')
    ax1.set_xlim([1.8,2.1])
    ax2.set_ylabel('Frequency (Hz)')
    ax2.set_xlabel('Time (s)')
    ax2.set_xlim([1.8,2.1])
       
    #window_size=[]
    #for i,value in enumerate(abs(strainh_data[f])):
    #    if value>=.1*np.amax(abs(strainh_data[f])):
    #        window_size.append(i)
    #ax1.set_xlim([strainh_time[f][1]*window_size[0],strainh_time[f][1]*window_size[-1]])
    #ax2.set_xlim([strainh_time[f][1]*window_size[0],strainh_time[f][1]*window_size[-1]])
        
    fh.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_1/q_'+str(qh_key[i])+'/strain_freq_plots/sfh_q'+str(qh_key[i])+'_inc_'+str(inch_key[i])+'_snr_'+str(snrh_key[i])+'.png')
    pl.close(fh)

#Residual Plot for Hanford detector data
for w in range(len(strainh_data)):
    fh,ax=pl.subplots()
    ax.plot(strainh_time[w],strainh_data[w]-injecth_data[w])
    ax.set_title('Hanford Residual data for q_'+str(qh_key[w])+'_inc_'+str(inch_key[w])+'_snr_'+str(snrh_key[w]))
    ax.set_ylabel('Residual Strain')
    ax.set_xlabel('Time (s)')
    ax.set_xlim([1.8,2.1])
    fh.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_1/q_'+str(qh_key[w])+'/residual_plots/rh_q'+str(qh_key[w])+'_inc_'+str(inch_key[w])+'_snr_'+str(snrh_key[w])+'.png')
    pl.close(fh)
    
#Strain/Frequency Plot for Livingston detector data
for g in range(len(strainl_data)):
    fl,(ax1,ax2)=pl.subplots(2, sharex=True)
    ax1.plot(strainl_time[g],strainl_data[g],color='r',label='Reconstruction')
    ax1.plot(strainl_time[g],injectl_data[g],color='b',label='Injection')
    ax1.legend(loc=2,fontsize='x-small')
    ax2.plot(freql_time[g],freql_data[g],color='r',label='Reconstruction')
    ax2.plot(freql_time[g],inject_freql_data[g],color='b',label='Injection')
    ax2.legend(loc=2,fontsize='x-small')
    ax1.set_title('Livingston Strain and Frequency data for q_'+str(ql_key[g])+'_inc_'+str(incl_key[g])+'_snr_'+str(snrl_key[g]))
    fl.subplots_adjust(hspace=0)
    ax1.set_ylabel('Strain')
    ax1.set_xlim([1.8,2.1])
    ax2.set_ylabel('Frequency (Hz)')
    ax2.set_xlabel('Time (s)')
    ax2.set_xlim([1.8,2.1])
    
    #window_size=[]
    #for j,value in enumerate(abs(strainl_data[g])):
    #    if value>=.1*np.amax(abs(strainl_data[g])):
    #        window_size.append(j)
    #ax1.set_xlim([strainl_time[g][1]*window_size[0],strainl_time[g][1]*window_size[-1]])
    #ax2.set_xlim([strainl_time[g][1]*window_size[0],strainl_time[g][1]*window_size[-1]])
    
    fl.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_1/q_'+str(ql_key[g])+'/strain_freq_plots/sfl_q'+str(ql_key[g])+'_inc_'+str(incl_key[g])+'_snr_'+str(snrl_key[g])+'.png')
    pl.close(fl)

#Residual Plot for Livingston detector data
for x in range(len(strainl_data)):
    fl,ax=pl.subplots()
    ax.plot(strainl_time[x],strainl_data[x]-injectl_data[x])
    ax.set_title('Livingston Residual data for q_'+str(ql_key[x])+'_inc_'+str(incl_key[x])+'_snr_'+str(snrl_key[x]))
    ax.set_ylabel('Residual Strain')
    ax.set_xlabel('Time (s)')
    ax.set_xlim([1.8,2.1])
    fl.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_1/q_'+str(ql_key[x])+'/residual_plots/rl_q'+str(ql_key[x])+'_inc_'+str(incl_key[x])+'_snr_'+str(snrl_key[x])+'.png')
    pl.close(fl)

#Window Size 2 (t=1.3-2.1)

#Strain/Frequency Plot for Hanford detector data
for j in range(len(strainh_data)):
    fh,(ax1,ax2)=pl.subplots(2, sharex=True)
    ax1.plot(strainh_time[j],strainh_data[j],color='r',label='Reconstruction')
    ax1.plot(strainh_time[j],injecth_data[j],color='b',label='Injection')
    ax1.legend(loc=2,fontsize='x-small')
    ax2.plot(freqh_time[j],freqh_data[j],color='r',label='Reconstruction')
    ax2.plot(freqh_time[j],inject_freqh_data[j],color='b',label='Injection')
    ax2.legend(loc=2,fontsize='x-small')
    ax1.set_title('Hanford Strain and Frequency data for q_'+str(qh_key[j])+'_inc_'+str(inch_key[j])+'_snr_'+str(snrh_key[j]))
    fh.subplots_adjust(hspace=0)
    ax1.set_ylabel('Strain')
    ax1.set_xlim([1.3,2.1])
    ax2.set_ylabel('Frequency (Hz)')
    ax2.set_xlabel('Time (s)')
    ax2.set_xlim([1.3,2.1])
   
    #window_size=[]
    #for i,value in enumerate(abs(strainh_data[f])):
    #    if value>=.1*np.amax(abs(strainh_data[f])):
    #        window_size.append(i)
    #ax1.set_xlim([strainh_time[f][1]*window_size[0],strainh_time[f][1]*window_size[-1]])
    #ax2.set_xlim([strainh_time[f][1]*window_size[0],strainh_time[f][1]*window_size[-1]])
    
    fh.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_2/q_'+str(qh_key[j])+'/strain_freq_plots/sfh_q'+str(qh_key[j])+'_inc_'+str(inch_key[j])+'_snr_'+str(snrh_key[j])+'.png')
    pl.close(fh)

#residual plot for hanford detector data
for y in range(len(strainh_data)):
    fh,ax=pl.subplots()
    ax.plot(strainh_time[y],strainh_data[y]-injecth_data[y])
    ax.set_title('hanford residual data for q_'+str(qh_key[y])+'_inc_'+str(inch_key[y])+'_snr_'+str(snrh_key[y]))
    ax.set_ylabel('residual strain')
    ax.set_xlabel('time (s)')
    ax.set_xlim([1.3,2.1])
    fh.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_2/q_'+str(qh_key[y])+'/residual_plots/rh_q'+str(qh_key[y])+'_inc_'+str(inch_key[y])+'_snr_'+str(snrh_key[y])+'.png')
    pl.close(fh)

#strain/frequency plot for livingston detector data
for n in range(len(strainl_data)):
    fl,(ax1,ax2)=pl.subplots(2, sharex=True)
    ax1.plot(strainl_time[n],strainl_data[n],color='r',label='reconstruction')
    ax1.plot(strainl_time[n],injectl_data[n],color='b',label='injection')
    ax1.legend(loc=2,fontsize='x-small')
    ax2.plot(freql_time[n],freql_data[n],color='r',label='reconstruction')
    ax2.plot(freql_time[n],inject_freql_data[n],color='b',label='injection')
    ax2.legend(loc=2,fontsize='x-small')
    ax1.set_title('livingston strain and frequency data for q_'+str(ql_key[n])+'_inc_'+str(incl_key[n])+'_snr_'+str(snrl_key[n]))
    fl.subplots_adjust(hspace=0)
    ax1.set_ylabel('strain')
    ax1.set_xlim([1.3,2.1])
    ax2.set_ylabel('frequency (hz)')
    ax2.set_xlabel('time (s)')
    ax2.set_xlim([1.3,2.1])
   
    #window_size=[]
    #for j,value in enumerate(abs(strainl_data[g])):
    #    if value>=.1*np.amax(abs(strainl_data[g])):
    #        window_size.append(j)
    #ax1.set_xlim([strainl_time[g][1]*window_size[0],strainl_time[g][1]*window_size[-1]])
    #ax2.set_xlim([strainl_time[g][1]*window_size[0],strainl_time[g][1]*window_size[-1]])
    
    fl.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_2/q_'+str(ql_key[n])+'/strain_freq_plots/sfl_q'+str(ql_key[n])+'_inc_'+str(incl_key[n])+'_snr_'+str(snrl_key[n])+'.png')
    pl.close(fl)

#Residual Plot for Livingston detector data
for z in range(len(strainl_data)):
    fl,ax=pl.subplots()
    ax.plot(strainl_time[z],strainl_data[z]-injectl_data[z])
    ax.set_title('Livingston Residual data for q_'+str(ql_key[z])+'_inc_'+str(incl_key[z])+'_snr_'+str(snrl_key[z]))
    ax.set_ylabel('Residual Strain')
    ax.set_xlabel('Time (s)')
    ax.set_xlim([1.3,2.1])
    fl.savefig('/home/bday7/nr_reconstructions/GW150914_bayeswave_runs/bayeswave/no_noise_runs/win_1/q_'+str(ql_key[z])+'/residual_plots/rl_q'+str(ql_key[z])+'_inc_'+str(incl_key[z])+'_snr_'+str(snrl_key[z])+'.png')
    pl.close(fl)

