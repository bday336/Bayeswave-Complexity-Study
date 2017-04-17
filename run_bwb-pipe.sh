#!/bin/bash
#
# Generate the workflow
#
export OSG_DEPLOY=TRUE
export BAYESWAVE_PREFIX=/cvmfs/oasis.opensciencegrid.org/ligo/pipeline/bayeswave/lscsoft/bayeswave-O2_online-r684
export LALSUITE_PREFIX=/cvmfs/oasis.opensciencegrid.org/ligo/pipeline/bayeswave/lscsoft/lalsuite-6.41
export BAYESWAVE_PIPE_PREFIX=/nv/hp11/jclark308/Projects/osg_tools/bwb
export LIGO_DATAFIND_SERVER="ligo-gftp.pace.gatech.edu:80"
source ${BAYESWAVE_PIPE_PREFIX}/etc/bayeswave-user-env.sh

bwb_pipe.py ${1}.ini \
    --workdir ${1} \
    --injfile HL-INJECTIONS-EOBNRv2HMpseudoFourPN-q_5-iota_0-snr_${2}.xml \
    --osg-jobs \
    --skip-datafind \
    --sim-data \
    --skip-megapy


