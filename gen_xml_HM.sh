#!/bin/bash
#

#
# Generate sim-inspiral table using lalapps_inspinj
#


seed=1150569646
#`lalapps_tconvert now`
#gpsstart=`lalapps_tconvert now`
gpsstart=1150569646
gpsend=$((${gpsstart} + 10000))

mtotal=100

for mass_ratio in 1
do

    mass2=`python -c "print float(${mtotal})/(1+${mass_ratio})"`
    mass1=`python -c "print ${mtotal}-${mass2}"`

    for inclination in 0 45 90 135 180 225 270 315 360
    do
	for SNR in 10 20 30 40 50
	do
        	outfile="HL-INJECTIONS-EOBNRv2HMpseudoFourPN-q_${mass_ratio}-iota_${inclination}-snr_${SNR}.xml"
        	lalapps_inspinj \
            	--seed ${seed} --f-lower 4 --gps-start-time ${gpsstart} \
            	--gps-end-time ${gpsend} --waveform EOBNRv2HMpseudoFourPN \
            	--time-step 100 --time-interval 10\
            	--l-distr random  \
            	--i-distr fixed --fixed-inc ${inclination} --disable-spin \
            	--m-distr fixMasses \
            	--fixed-mass1 ${mass1} --fixed-mass2 ${mass2}\
            	--output ${outfile} \
            	--snr-distr volume \
            	--min-snr ${SNR} --max-snr ${SNR} \
            	--ligo-fake-psd LALAdLIGO \
            	--ligo-start-freq 16 \
            	--ifos H1,L1 --verbose #--taper-injection start
	done
    done

done
