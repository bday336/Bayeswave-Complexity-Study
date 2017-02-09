#!/bin/bash/

import os
import numpy as np
from matplotlib import pyplot as pl

#Setup data caches

med_overlap_inc0h=[]
snr_inc0h=[]
med_overlap_inc0l=[]
snr_inc0l=[]
med_overlap_inc45h=[]
snr_inc45h=[]
med_overlap_inc45l=[]
snr_inc45l=[]
med_overlap_inc90h=[]
snr_inc90h=[]
med_overlap_inc90l=[]
snr_inc90l=[]
med_overlap_inc135h=[]
snr_inc135h=[]
med_overlap_inc135l=[]
snr_inc135l=[]

#Load the data from each reconstruction waveform directory
for a in os.listdir(os.getcwd()):
    if 'inc_0' in a or 'inc_45' in a or 'inc_90' in a or 'inc_135' in a:
        for b in os.listdir(os.getcwd()+'/'+str(a)):
            if 'inc_0_snr' in b and '.ini' not in b or 'inc_45_snr' in b and '.ini' not in b or 'inc_135_snr' in b and '.ini' not in b:
                for c in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)):
                    if 'bayeswave_1150569652' in c:
                        for d in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)):
                            if 'post' in d and 'bay' not in d:
                                for e in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)):
                                    #Reconstruction median overlap for Hanford detector
                                    if 'signal_whitened_moments.dat.0' in e:
                                        if 'inc_0' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc0h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc0h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc0h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc0h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc0h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc0h.append(50)
                                        elif 'inc_45' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc45h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc45h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc45h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc45h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc45h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc45h.append(50)
                                        elif 'inc_90' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc90h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc90h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc90h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc90h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc90h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc90h.append(50)
                                        elif 'inc_135' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc135h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc135h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc135h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc135h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc135h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc135h.append(50)
                                    #Reconstruction median overlap for Livingston detector
                                    elif 'signal_whitened_moments.dat.1' in e:
                                        if 'inc_0' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc0l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc0l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc0l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc0l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc0l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc0l.append(50)
                                        elif 'inc_45' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc45l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc45l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc45l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc45l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc45l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc45l.append(50)
                                        elif 'inc_90' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc90l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc90l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc90l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc90l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc90l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc90l.append(50)
                                        elif 'inc_135' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            med_overlap_inc135l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc135l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc135l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc135l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc135l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc135l.append(50)

#Plot median overlap as function of SNR for the various
# inclinations that are being tested which are
# 0 degrees to 360 degrees in increments of 90 degrees

#Plot of median overlap as function of SNR for Hanford detector 
fh=pl.figure()
pl.scatter(snr_inc0h,med_overlap_inc0h,color='r',label='inc=0')
pl.scatter(snr_inc45h,med_overlap_inc45h,color='b',label='inc=45')
pl.scatter(snr_inc90h,med_overlap_inc90h,color='m',label='inc=90')
pl.scatter(snr_inc135h,med_overlap_inc135h,color='k',label='inc=135')
fh.suptitle('Median overlap for Hanford')
pl.ylabel('Median overlap')
pl.xlabel('SNR')
pl.legend(loc='lower right')
pl.show()
pl.close()

#Plot of median overlap as function of SNR for Livingston detector
fl=pl.figure()
pl.scatter(snr_inc0l,med_overlap_inc0l,color='r',label='inc=0')
pl.scatter(snr_inc45l,med_overlap_inc45l,color='b',label='inc=45')
pl.scatter(snr_inc90l,med_overlap_inc90l,color='m',label='inc=90')
pl.scatter(snr_inc135l,med_overlap_inc135l,color='k',label='inc=135')
fl.suptitle('Median overlap for Livingston')
pl.ylabel('Median overlap')
pl.xlabel('SNR')
pl.legend(loc='lower right')
pl.show()
pl.close()

