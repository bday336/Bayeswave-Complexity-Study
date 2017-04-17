#!/bin/bash/

import os
import numpy as np
from matplotlib import pyplot as pl
from matplotlib import colors as col

#Setup data caches

med_overlap_inc0h=[]
overlap_inc0h=[]
snr_inc0h=[]
med_overlap_inc0l=[]
overlap_inc0l=[]
snr_inc0l=[]

med_overlap_inc45h=[]
overlap_inc45h=[]
snr_inc45h=[]
med_overlap_inc45l=[]
overlap_inc45l=[]
snr_inc45l=[]

med_overlap_inc90h=[]
overlap_inc90h=[]
snr_inc90h=[]
med_overlap_inc90l=[]
overlap_inc90l=[]
snr_inc90l=[]

med_overlap_inc135h=[]
overlap_inc135h=[]
snr_inc135h=[]
med_overlap_inc135l=[]
overlap_inc135l=[]
snr_inc135l=[]

med_overlap_inc180h=[]
overlap_inc180h=[]
snr_inc180h=[]
med_overlap_inc180l=[]
overlap_inc180l=[]
snr_inc180l=[]

med_overlap_inc225h=[]
overlap_inc225h=[]
snr_inc225h=[]
med_overlap_inc225l=[]
overlap_inc225l=[]
snr_inc225l=[]

med_overlap_inc270h=[]
overlap_inc270h=[]
snr_inc270h=[]
med_overlap_inc270l=[]
overlap_inc270l=[]
snr_inc270l=[]

med_overlap_inc315h=[]
overlap_inc315h=[]
snr_inc315h=[]
med_overlap_inc315l=[]
overlap_inc315l=[]
snr_inc315l=[]

med_overlap_inc360h=[]
overlap_inc360h=[]
snr_inc360h=[]
med_overlap_inc360l=[]
overlap_inc360l=[]
snr_inc360l=[]

#Load the data from each reconstruction waveform directory
for a in os.listdir(os.getcwd()):
    if 'inc_0' in a or 'inc_45' in a or 'inc_90' in a or 'inc_135' in a or 'inc_180' in a or 'inc_225' in a or 'inc_270' in a or 'inc_315' in a or 'inc_360' in a:
        for b in os.listdir(os.getcwd()+'/'+str(a)):
            if 'inc_0_snr' in b and '.ini' not in b or 'inc_45_snr' in b and '.ini' not in b or 'inc_90_snr' in b and '.ini' not in b or 'inc_135_snr' in b and '.ini' not in b or 'inc_180_snr' in b and '.ini' not in b or 'inc_225_snr' in b and '.ini' not in b or 'inc_270_snr' in b and '.ini' not in b or 'inc_315_snr' in b and '.ini' not in b or 'inc_360_snr' in b and '.ini' not in b:
                for c in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)):
                    if 'bayeswave_1150569652' in c:
                        for d in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)):
                            if 'post' in d and 'bay' not in d:
                                for e in os.listdir(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)):
                                    #Reconstruction median overlap for Hanford detector
                                    if 'signal_whitened_moments.dat.0' in e:
                                        if 'inc_0' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc0h.append(raw_data_h[:,7])
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
                                            overlap_inc45h.append(raw_data_h[:,7])
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
                                            overlap_inc90h.append(raw_data_h[:,7])
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
                                            overlap_inc135h.append(raw_data_h[:,7])
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
                                        elif 'inc_180' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc180h.append(raw_data_h[:,7])
                                            med_overlap_inc180h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc180h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc180h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc180h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc180h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc180h.append(50)
                                        elif 'inc_225' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc225h.append(raw_data_h[:,7])
                                            med_overlap_inc225h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc225h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc225h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc225h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc225h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc225h.append(50)
                                        elif 'inc_270' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc270h.append(raw_data_h[:,7])
                                            med_overlap_inc270h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc270h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc270h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc270h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc270h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc270h.append(50)
                                        elif 'inc_315' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc315h.append(raw_data_h[:,7])
                                            med_overlap_inc315h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc315h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc315h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc315h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc315h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc315h.append(50)
                                        elif 'inc_360' in a:
                                            raw_data_h=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc360h.append(raw_data_h[:,7])
                                            med_overlap_inc360h.append(np.median(raw_data_h[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc360h.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc360h.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc360h.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc360h.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc360h.append(50)
                                    #Reconstruction median overlap for Livingston detector
                                    elif 'signal_whitened_moments.dat.1' in e:
                                        if 'inc_0' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc0l.append(raw_data_h[:,7])
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
                                            overlap_inc45l.append(raw_data_h[:,7])
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
                                            overlap_inc90l.append(raw_data_h[:,7])
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
                                            overlap_inc135l.append(raw_data_h[:,7])
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
                                        elif 'inc_180' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc180l.append(raw_data_h[:,7])
                                            med_overlap_inc180l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc180l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc180l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc180l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc180l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc180l.append(50)
                                        elif 'inc_225' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc225l.append(raw_data_h[:,7])
                                            med_overlap_inc225l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc225l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc225l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc225l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc225l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc225l.append(50)
                                        elif 'inc_270' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc270l.append(raw_data_h[:,7])
                                            med_overlap_inc270l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc270l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc270l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc270l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc270l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc270l.append(50)
                                        elif 'inc_315' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc315l.append(raw_data_h[:,7])
                                            med_overlap_inc315l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc315l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc315l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc315l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc315l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc315l.append(50)
                                        elif 'inc_360' in a:
                                            raw_data_l=np.loadtxt(os.getcwd()+'/'+str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'/'+str(e))
                                            overlap_inc360l.append(raw_data_h[:,7])
                                            med_overlap_inc360l.append(np.median(raw_data_l[:,7]))
                                            if 'snr_10' in b:
                                                snr_inc360l.append(10)
                                            elif 'snr_20' in b:
                                                snr_inc360l.append(20)
                                            elif 'snr_30' in b:
                                                snr_inc360l.append(30)
                                            elif 'snr_40' in b:
                                                snr_inc360l.append(40)
                                            elif 'snr_50' in b:
                                                snr_inc360l.append(50)

#Plot median overlap as function of SNR for the various
# inclinations that are being tested which are
# 0 degrees to 360 degrees in increments of 90 degrees

#Plot of median overlap as function of SNR for Hanford detector 
fh=pl.figure()
pl.errorbar(snr_inc0h,med_overlap_inc0h,yerr=np.std(overlap_inc0h),ls='none',marker='o',color='r',label='inc=0')
pl.errorbar(snr_inc45h,med_overlap_inc45h,yerr=np.std(overlap_inc45h),ls='none',marker='v',color='b',label='inc=45')
pl.errorbar(snr_inc90h,med_overlap_inc90h,yerr=np.std(overlap_inc90h),ls='none',marker='^',color='m',label='inc=90')
pl.errorbar(snr_inc135h,med_overlap_inc135h,yerr=np.std(overlap_inc135h),ls='none',marker='<',color='k',label='inc=135')
pl.errorbar(snr_inc180h,med_overlap_inc180h,yerr=np.std(overlap_inc180h),ls='none',marker='>',color='g',label='inc=180')
pl.errorbar(snr_inc225h,med_overlap_inc225h,yerr=np.std(overlap_inc225h),ls='none',marker='p',color='c',label='inc=225')
pl.errorbar(snr_inc270h,med_overlap_inc270h,yerr=np.std(overlap_inc270h),ls='none',marker='s',color='salmon',label='inc=270')
pl.errorbar(snr_inc315h,med_overlap_inc315h,yerr=np.std(overlap_inc315h),ls='none',marker='*',color='darkorchid',label='inc=315')
pl.errorbar(snr_inc360h,med_overlap_inc360h,yerr=np.std(overlap_inc360h),ls='none',marker='D',color='grey',label='inc=360')
fh.suptitle('Median Overlap for q=1 Hanford Data')
pl.ylabel('Median overlap')
pl.xlabel('SNR')
pl.legend(loc='lower right',fontsize='x-small')
pl.show()
pl.close()

#Plot of median overlap as function of SNR for Livingston detector
fl=pl.figure()
pl.errorbar(snr_inc0l,med_overlap_inc0l,yerr=np.std(overlap_inc0l),ls='none',marker='o',color='r',label='inc=0')
pl.errorbar(snr_inc45l,med_overlap_inc45l,yerr=np.std(overlap_inc45l),ls='none',marker='v',color='b',label='inc=45')
pl.errorbar(snr_inc90l,med_overlap_inc90l,yerr=np.std(overlap_inc90l),ls='none',marker='^',color='m',label='inc=90')
pl.errorbar(snr_inc135l,med_overlap_inc135l,yerr=np.std(overlap_inc135l),ls='none',marker='<',color='k',label='inc=135')
pl.errorbar(snr_inc180l,med_overlap_inc180l,yerr=np.std(overlap_inc180l),ls='none',marker='>',color='g',label='inc=180')
pl.errorbar(snr_inc225l,med_overlap_inc225l,yerr=np.std(overlap_inc225l),ls='none',marker='p',color='c',label='inc=225')
pl.errorbar(snr_inc270l,med_overlap_inc270l,yerr=np.std(overlap_inc270l),ls='none',marker='s',color='salmon',label='inc=270')
pl.errorbar(snr_inc315l,med_overlap_inc315l,yerr=np.std(overlap_inc315l),ls='none',marker='*',color='darkorchid',label='inc=315')
pl.errorbar(snr_inc360l,med_overlap_inc360l,yerr=np.std(overlap_inc360l),ls='none',marker='D',color='grey',label='inc=360')
fl.suptitle('Median Overlap for q=1 Livingston Data')
pl.ylabel('Median overlap')
pl.xlabel('SNR')
pl.legend(loc='lower right',fontsize='x-small')
pl.show()
pl.close()

