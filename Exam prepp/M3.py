##ordinary exam 2025 

from functools import reduce
import numpy as np

def A5_old(zip_exam): ##Exercise A5
    grade_A5 = []
    for name_grade in zip_exam:
        if name_grade[1] == 5:
            grade_A5.append(name_grade[0])
    return grade_A5
def A5(zip_exam): ##Exercise A5
    top = filter(lambda name_grade: name_grade[1] ==5, zip_exam)
    return list(map(lambda name_grade: name_grade[0], top))
    
    
def generate_list(n):
    a = np.random.randint(0,9)
    b = np.random.randint(10, 19)
    return np.random.uniform(a,b,n)


def generate_list(n):
    a = np.random.randint(0,9)
    b = np.random.randint(10, 19)
    return np.random.uniform(a,b,n)


def Estimation(lst): ##Exercise A6
    n = len(lst)
    n_p = 10
    
import concurrent.futures as future
import numpy as np
def Estimation(lst): ##Exercise A6
    n = len(lst) #exc6 estimation of unkown interval
    n_p = 10
    reshaped = lst.reshape(n_p, -1)
    ##lst => array. n_p tells it to use 10 rows,
    # -1 is shorthand for calculate dimension automatically
    with future.ProcessPoolExecutor() as ex:
        minimals = ex.map(min, reshaped)
        maximals = ex.map(max, reshaped)
        minimals = list(minimals)
        maximals = list(maximals)
    total_min = min(minimals)
    total_max = max(maximals)
    return n/(n-1)*total_min - 1/(n-1)*(total_max), n/(n-1)*total_max - 1/(n-1)*(total_min)


def main():

    print("Test A5:")
    names = ["Anna", "Anton", "Jakob",
    "Ludwig", "Nils", "Oliver",
    "Rafael", "Tim"]
    grades = [3,4,5,5,4,3,5,5]
    #for l, f in zip(names, grades):
       # print(f'{l} receives {f}')
    print(A5(zip(names, grades)))
    print("Test A6:")
    n = 10**6
    lst = generate_list(n)
    print(Estimation(lst))
if __name__ == '__main__':
    pass 
    #main()


#re-rexam VT 2025
#A5



import math 

def is_prime(n):
    """ Returns true if n is prime
    """
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime

from functools import reduce 
def sum_prime_old(x): ##Exercise A5
    lst_of_nums = [x for x in range (0, x)]
    lst_of_primes = list(map(lambda x: is_prime(x), lst_of_nums))
    print(lst_of_primes)


def sum_prime(x): ##Exercise A5
    #list comp: [what_to_store for item in iterable if condition
    lst_of_primes = [n for n in range (0, x) if is_prime(n) == True]
    return reduce(lambda total, num: total + num, lst_of_primes, 0)
    ## the zero in the return line is a default value for reduce


def test_sum_prime():
    for x in [4 , 5 , 6 , 7 , 100 , 1000]:
        print ( sum_prime ( x ) , end = " " )

#test_sum_prime()


def generate_normal(n):
    a = np.random.randint(0,9)
    b = np.random.randint(1, 10)
    return np.random.normal(a,b,n)

import numpy as np
import concurrent.futures as future
def Estimation(arr): ##Exercise A6, find the mean
    n_p = 10 #number of proccesses
    reshaped = arr.reshape(n_p, -1)
    with future.ProcessPoolExecutor() as ex:
        total = list(ex.map(sum, reshaped)) 
    return sum(total) / (len(arr))


def main():

    print("Test A5:")
    for x in [4, 5, 6, 7, 100, 1000]:
        print(sum_prime(x), end=" ")
    print("\nTest A6:")
    n = 10**6
    arr = generate_normal(n)
    print(Estimation(arr))
if __name__ == '__main__':
    main()
    


