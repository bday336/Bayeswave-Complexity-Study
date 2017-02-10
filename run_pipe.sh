#!/bin/bash

# Here the argument is name of the .ini file corresponding to the
# specific injection file that is being prepared for the 
# Bayeswave Analysis.

bwb_pipe.py ${1}.ini \
    --user-tag ${1} \
    --workdir ${1} \
    --sim-data
