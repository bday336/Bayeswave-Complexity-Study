#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <math.h>

void tf_tracks(double *hoft, double *frequency_out, double deltaT, int Nsample);
void interp_tf(double **tf, double **pts, int tlength, int Nsample);

int main()
{

    int srate=1024;
    //int srate=16384;
    double duration=4;
    double deltaT=1/(double)srate;
    printf("%lg\n", deltaT);

    int Nsample=srate*duration;
    fprintf(stdout, "Nsample=%d\n", Nsample);

    double *times = malloc(Nsample*sizeof(double));
    double *median_hoft = malloc(Nsample*sizeof(double));
    double *frequencies = malloc(Nsample*sizeof(double));

    FILE *fp_in, *fp_out;
    char infile[100];
    char outfile[100];
    int i, j;
    int Nifos=2;

    printf("loading data\n");
    for (i=0; i<Nifos; i++){
	fprintf(stdout, "injected_whitened_waveform.dat.%d\n", i);
        sprintf(infile,"injected_whitened_waveform.dat.%d", i);
        //sprintf(infile,"G187068-IMRPhenomPv2-hwinj.dat.%d",i);
        fp_in = fopen(infile, "r");
        for (j = 0; j < Nsample; j++){
            //fscanf(fp_in, "%lg %lg", &times[j], &median_hoft[j]);
            fscanf(fp_in, "%lg", &median_hoft[j]);
        }
        fclose(fp_in);

        printf("computing frequencies from zero crossings\n");
        tf_tracks(median_hoft, frequencies, deltaT, Nsample);

        sprintf(outfile, "injected_median_tf.dat.%d",i);
        //sprintf(outfile, "G187068-IMRPhenomPv2-tftrack.dat.%d",i);
        fp_out = fopen(outfile, "w");
        for (j = 0; j < Nsample; j++){
	    //fprintf(stdout, "%lg %lg\n", times[j], frequencies[j]);
            //fprintf(fp_out, "%lg %lg\n", times[j], frequencies[j]);
	    fprintf(stdout, "%lg\n", frequencies[j]);
            fprintf(fp_out, "%lg\n", frequencies[j]);
        }
        fclose(fp_out);
    }


}


void tf_tracks(double *hoft, double *frequency_out, double deltaT, int N){
    int i, ii, jj;
    
    double slope, intercept, zero, freq;
    
    double *w    = malloc(N*sizeof(double));
    double **tf_raw = malloc(2*sizeof(double *));
    double **tf_track = malloc(2*sizeof(double *));
    double *zerotimes = malloc(N*sizeof(double));
    
    for (i = 0; i < 2; i++) {
        tf_raw[i] = malloc(N*sizeof(double));
        tf_track[i] = malloc(N*sizeof(double));
    }
    
    for (ii = 0; ii < N; ii++) {
        tf_track[0][ii] = (double)ii*deltaT;
    }
    
    jj = 0;
    
    //get_time_domain_waveforms(hoft, w, N, imin, imax);
    
    // Get f of t from zero crossings
    for (ii = 0; ii <= 2; ii++) {
        zerotimes[ii] = 0.0;
    }
    
    
    for (ii = 0; ii < N-1; ii++) {
        // find where it crosses
        if (hoft[ii]*hoft[ii+1] < 0.0) {
            
            slope = (hoft[ii+1] - hoft[ii])/deltaT; // rise over run
            intercept = hoft[ii] - slope*(double)ii*deltaT; // y = mx + b;
            zero = -intercept/slope; // gives t value of zero;
            
            
            // update crossing points (ie "current" "previous" and "next")
            zerotimes[2] = zerotimes[1];
            zerotimes[1] = zerotimes[0];
            zerotimes[0] = zero;
            
            // Find the frequency at each zero crossing
            if (jj > 3) {
                freq = (1./(zerotimes[0]-zerotimes[2]));
                tf_raw[0][jj] = zerotimes[1];
                
                //printf("%g\n",tf[1][jj]);
                tf_raw[1][jj] = freq;
                
                
            }
            else{
                tf_raw[0][jj] = zerotimes[1];
                tf_raw[1][jj] = 0.0;
            }
            jj++; // this gives the number of tf points we have
        }
    }
    
    
    
    // Interpolate
    interp_tf(tf_track, tf_raw, jj, N);
    
    for (ii = 0; ii < N; ii++) {
        frequency_out[ii] = tf_track[1][ii];
    }
    
    
    for (ii=0; ii<2; ii++) {
        free(tf_raw[ii]);
        free(tf_track[ii]);
    
    }
    
    free(w);
    free(zerotimes);
    free(tf_raw);
    free(tf_track);
    
    
}

void interp_tf(double **tf, double **pts, int tlength, int Nsample){
    int ii, jj;
    double slope, intercept;
    
    
    ii = 2;
    for (jj = 0; jj < Nsample; jj++) {
        
        while ((pts[0][ii] < tf[0][jj] || fabs(pts[0][ii-1]-pts[0][ii]) < 1e-7 /* sometimes points too close together gets fucked up*/) && ii < tlength) {
            ii++; // this just figures out which two points we're interpolating between
        }
        
        slope = (pts[1][ii]-pts[1][ii-1])/(pts[0][ii]-pts[0][ii-1]);
        intercept = pts[1][ii] - slope*pts[0][ii]; // y = mx + b;
        tf[1][jj] = slope*tf[0][jj]+intercept; // assign frequency
        
        
        
    }
    
    
}


