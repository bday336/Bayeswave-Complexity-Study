CC=gcc
CCFLAGS=

all: bayeswave_tftrack

bayeswave_tftrack : bayeswave_tftrack.c
	$(CC) $(CCFLAGS) -o bayeswave_tftrack bayeswave_tftrack.c

clean:
	rm bayeswave_tftrack

