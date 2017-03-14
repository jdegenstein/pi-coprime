from joblib import Parallel, delayed
import multiprocessing
import numpy

num_cores = multiprocessing.cpu_count()

inputs = range(num_cores) #set number of runs to number of threads


def randomPIE(i):
    import random
    import math

    # I put these here so you can change them easily
    MAX = 99999999 # highest random number
    COUNT = 10000000 # number of pairs the program generates

    coprime = 0
    cofactor = 0

    for t in range(COUNT):
        a = random.randint(1, MAX)
        b = random.randint(1, MAX)

        # Euclidean Algorithm - many  times faster than checking every number from 2 to min(a, b)
        while b != 0:
            temp = b
            b = a % b
            a = temp

        # a is now the GCD of the two random numbers
        if a == 1:
            coprime += 1
        else:
            cofactor += 1
    return math.sqrt(6/(coprime/COUNT)) #approximately equal to Pi!!!

#parallelize
results = Parallel(n_jobs=num_cores)(delayed(randomPIE)(i) for i in inputs)


print('pi is approx. ' + str(numpy.mean(results)))
