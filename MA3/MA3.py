""" MA3.py

Student:lars kirchner 
Mail: lasse.kirchner@gmail.com
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
from functools import reduce 
import concurrent.futures as future
import multiprocessing as mp 

# Exc1
def approximate_pi(n):
    # n is the number of points
    total = 0  
    n_out = 0 #outside
    n_in = 0 
    while n_out + n_in != n:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if m.sqrt(x**2 + y**2) > 1:
            n_out += 1
        else:
            n_in += 1 
    return 4*((n_in)/n)



# Exc2, approximation
def sphere_volume(n, d): 
    # n is the number of points
    # d is the number of dimensions of the sphere 
    n_out = 0
    n_in = 0 
    volume_container = (1 + 1)**d #assume r = 1
    dims = [x for x in range (0, d)]
    
    while n_out + n_in != n:
        temp_position = [random.uniform(-1, 1) for dim in dims] # list comp. 

        #map takes a function and applies it to every single item in a list, returning a new modified list.
        #A lambda function is just a shorthand way to write a small, one-line function without giving it a name. 
        squared_temp_pos = list(map(lambda x: x**2, temp_position))

        #reduce() takes a list of items and squashed them down into a single final value
        # by repeadetly applying a calculation pair-by-pair.
        if reduce(lambda acc, x: x + acc, squared_temp_pos) <= 1: #avstånd mindre än 1 l.e.
            n_in += 1
        else:
            n_out += 1 
    return ((n_in/n)*volume_container)
    ##higher order functions used: lambda, reduce and list comp. 


#Exc2, real value 
def hypersphere_exact_old(d):
    # n is the number of points
    # d is the number of dimensions of the sphere
    ##ill assume that r = 1 
    gamma_numerator = m.pi**((d)/2) 
    gamma_denominator = m.gamma(1+ (d)/2)
    return gamma_numerator/gamma_denominator
    #can be done in one line but this makes it clearer for me! 

    '''
    print(f'The exact volume for a {d} dimensional hypersphere is:') 
    print(calc_vol(d))''' # if the testfunction isnt an okay solution 

def hypersphere_exact(n, d):
    return (m.pi**((d)/2))/(m.gamma(1+ (d)/2)) ##klarar ej test två, men test två känns stupid 


from numba import njit 
#Exc3: numba version
@njit ##calls numba module to convert function itno machine code 
def sphere_volume_numba(n:int, d:int)->float:
    # n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes

    ##copied from ex1
    n_out = 0
    n_in = 0 
    volume_container = (1 + 1)**d #assume r = 1
    dims = [x for x in range (0, d)]
    
    while n_out + n_in != n:
        temp_position = [random.uniform(-1, 1) for dim in dims]
        squared_temp_pos = list(map(lambda x: x**2, temp_position))
        if reduce(lambda acc, x: x + acc, squared_temp_pos) <= 1: #avstånd mindre än 1 l.e.
            n_in += 1
        else:
            n_out += 1 
    return ((n_in/n)*volume_container)


#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel_using_mp(n, d, np=10):
    # n is the number of points
    # d is the number of dimensions of the sphere
    # np is the number of processes
    #start_time = pc()

    processes = []
    for _ in range(0, np):
        p = mp.Process(target=sphere_volume, args=[n, d])
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    #end_time = pc()
    #return print(f'Process took: {round((end_time-start_time), 3)} seconds using paralell computing.')
    return print(f'Returnerar inget, måste göra om :()')

import concurrent.futures as future
def sphere_volume_parallel (n, d, np=10):
    with future.ProcessPoolExecutor() as ex:
        lst_temp_n = []
        lst_temp_d = []
        for i in range(0, np):
            lst_temp_n.append(n / np)
            lst_temp_d.append(d)
    
        results = ex.map(sphere_volume, lst_temp_n, lst_temp_d)

        total_vol = 0
        for i in results:
            total_vol += i
        return total_vol / np 


def sphere_volume_parallel_numba (n, d, np=10):
    with future.ProcessPoolExecutor() as ex:
        lst_temp_n = []
        lst_temp_d = []
        for i in range(0, np):
            lst_temp_n.append(n / np)
            lst_temp_d.append(d)
    
        results = ex.map(sphere_volume_numba, lst_temp_n, lst_temp_d)

        total_vol = 0
        for i in results:
            total_vol += i
        return total_vol / np 


def main():
    # Exc1
    def test_ex1():
        dots = [1000, 10000, 100000]
        for n in dots:
            return print(approximate_pi(n))
        

    #test_ex1()

    # Exc2 ## old test 2 function, dosent relly seem appropriate to use
    def test_ex2_Old():
        n = 100000
        d = 2
        sphere_volume(n, d)
        print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

        n = 100000
        d = 11
        sphere_volume(n, d)
        print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    #test_ex2_old()

    def test_ex2_new():
        n = 100000
        d = 2
        sphere_estimate = round(sphere_volume(n, d), 4)
        sphere_exact = round(hypersphere_exact(d), 4)

        print(f'Volume of {d}-dim sphere with n={n}:')
        print(f'estimated = {sphere_estimate}, exact = {sphere_exact} \n') 

        # Test Case 2: 11D
        n = 100000
        d = 11
        sphere_estimate = round(sphere_volume(n, d), 4)
        sphere_exact = round(hypersphere_exact(d), 4)

        print(f'Volume of {d}-dim sphere with n={n}: estimated = {sphere_estimate},') 
        print(f'Exact volume = {sphere_exact}')

    #test_ex2_new()

    # Exc3 ## 
    def test_ex3_old():
        n = 1000000
        d = 11
        print('Exc3 analysis')
        start = pc()
        sphere_volume(n, d)
        stop = pc()
        print(f'Sequential time of d = {d} and n = {n}: \n')
        print(f'{round(stop-start, 4)}')
        print(f"What is numba time for d = {d} and n = {n}:?")
        start = pc()
        sphere_volume_numba(n, d)
        stop = pc() 
        print(f'{round(stop-start, 4)}')

    

    def better_run_test_exc3():
        n = 1000000
        d = 11
        print('Exc3 analysis:')
        print(f'Using a d = {d} dimensional sphere and n = {n}.')
        def inner():
            start = pc()
            sphere_volume(n, d)
            stop = pc()
            print(f'Sequential: {round(stop-start, 4)} seconds')
            start = pc()
            sphere_volume_numba(n, d)
            stop = pc() 
            print(f'Numba: {round(stop-start, 4)} seconds ')


        for i in range (1,4):
            print(f'TIMES FOR call number {i}:')
            inner()
    #better_run_test_exc3()

    # Exc4
    def test_ex4():
        n = 1000000
        d = 11
        start = pc()
        sphere_volume(n, d)
        stop = pc()
        print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
        print("What is parallel time?")
        start_paralell = pc()
        sphere_volume_parallel(10**6, 11)
        stop_paralell = pc()
        print(f'Parallel time regular is: {round(stop_paralell-start_paralell, 3)} seconds')
        start_numba = pc()
        sphere_volume_parallel_numba(n, d)
        stop_numba = pc() 
        print(f'Parallel time numba is: {round(stop_numba-start_numba, 3)} seconds')



    test_ex4()
    
'''Exc4: Sequential time of 11 and 1000000: 16.234666429983918
What is parallel time?
Process took: 1.886 seconds using paralell computing (via gullviva).
(venv) laki0611@gullviva:~/prog2/MA3$'''

'''with numba: '''

#hejhej

if __name__ == '__main__':
    main()
