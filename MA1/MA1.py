"""
Solutions to module 1
Student: 
E-mail:
Reviewed by:
Review date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have test code running at the top level (i.e. outside the main function),
you have to remove it before uploading your code into Studium!
Also remove any trace and debugging printouts!

You may not import any packages other than time and math. These may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documentation and and don't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""

import time
import math
#excersice 1 
#idea for ex1: take for ex 3*2 = 3+3 or 2+2+2
def multiply(m: int, n: int) -> int:
    if m < 0:
        return print('Arguments should be positive integers! Adjust value of m!')
    if n < 0:
        return print('Arguments should be positive integers! Adjust value of n!')
    if n>= m:
        if n == 0:
            return 0
        else:           
            return (m+multiply(m, n-1))
    else:
        if m == 0:
           return 0
        else:           
            return (n+multiply(m-1, n))
          
'''print(multiply(10, 10))
print(multiply(6, 7))'''
#for more effective code: check if n or m is larger, and use the smallest to iterate

#ex2 Computes and returns the harmonic sum 1 + 1/2 + 1/3 + ... + 1/n"""
def harmonic(n: int) -> float:   
    if n == 1:
        return 1
    else:
        return (1/n) + (harmonic(n-1))

'''Ex3 get binary!'''
def get_binary(x: int) -> str:   
    if x< 0:
        return '-' + get_binary(-x)
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    elif x > 1:
        return get_binary(x//2) + str(x%2)


"""Exc4: Returns the string s reversed """
def reverse_string(s: str) -> str:
    x = len(s)
    if x == 0:
        return ''
    if x == 1:
        return f'{s[0]}'
    else:
        return s[-1] + reverse_string(s[0:x-1]) 
#print(reverse_string('Hejhej'))


#ex5
def largest(a: list):

    if len(a) == 1:
        return a[0]

    if type(a[0]) == list: # hanterar nestlade listor
        return largest(a(0))

    memory = largest(a[1:])
    if a[0] > memory:
        return a[0]
    else:
        return memory 

'''Write a recursive function count(x, s) which counts and returns how many
times x appears at the top of list s or one of its sub-lists.
Example: The call count(4, [1, 4, 2, ['a', [[4], 3, 4]]]) should return 1.
Then modify the code to count instances at all levels. The call above should
then return 3.
Hint: The expression type(x) == list returns True if x is a list, otherwise
False.
Requirements: Make sure that lists are not destroyed. Searching of non-
existing elements should return 0'''
"""Exc6: Counts the number of occurences of x on all levels in s"""
#idea: use largest but modify res to count(?)
def count(x, s: list) -> int:   
    
    if len(s) == 0: # list is empty, cant contain anything
        return 0
    elif s[0] == x:
        return 1 + count(x, s[1:]) 
    elif type(s[0]) == list:
        return count (x, s[0]) + count(x, s[1:])
    return count(x, s[1:])

"""Exc7: Returns a list of string instructions for how to move the tiles"""
##also called tower of hanoi
##cant seem to get down to five lines without removing the if n == 0 
def bricklek(f: str, t: str, h: str, n: int) -> list[str]:
    ans = []
    if n == 0:
        return ans
    ans.extend(bricklek(f, h, t, n-1))  ## get step 1 into ans
    ans.append(f'{f}->{t}')  #step 2, move largest
    ans.extend(bricklek(h, t, f, n-1)) # move all except largest onto largest, #change which pegs are goal, helper, etc. 
    return ans

def own_test_bricklek():
    print(bricklek('f', 't', 'h', 1)) #tests base-case
    print(bricklek('f', 't', 'h', 2))
    print(bricklek('f', 't', 'h', 4))

#own_test_bricklek()


"""For Exc9: Returns the n:th Fibonacci number"""
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!

def fib(n: int) -> int:                      

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n):
    memory = {0:0, 1:1}

    def _fib_mem(n):
        if n not in memory:
            memory[n] = _fib_mem(n-1) + _fib_mem(n-2)
        return memory[n]
    
    return _fib_mem(n)


import unittest
import time
def main():

    def test_coding():
        print('\nCode that demonstrates my implementations\n')
        print('Tests functions 1-7 using given tests\n')

        ## unitest, four rows below generated using chat GTP.
        loader = unittest.TestLoader()
        suite = loader.discover('.', pattern='MA1_test_*.py')
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        ## end tests 1-7

    test_coding()

    def calculate_hanoi_50():
        print('\n Analysis of Tower of Hanoi: \n' \
        'If we want to know how long it would take to perform a round with \n' \
        '50 blocks, we must first find a way of expressing the required moves \n' \
        'as a function of the number of blocks.')
        print('The number of required moves is proportional to (2^n) -1' \
        ' where n is the number of blocks.')
        print('Assuming each move takes one second to perform:')
        time_sec = -1 + 2**50
        print(f'It takes {time_sec} seconds, or {round(time_sec/(60*60*24*365), 2)} years(!) to complete the game with 50 blocks! \n')

    calculate_hanoi_50()

    def fib_test():
        print('Analysis of time needed for the 50th and 100th fibbonacci number:')
        factors  = [] #takes the times for five following fib numbers! 
        def get_fib_times(n): #we want to se a factor of roughly 1.618^n in difference
            start = time.perf_counter()
            print('Fib number: ---------- Time:')
            nth_fib = fib(n)
            running = time.perf_counter() - start ##important that its after the fib call!!
            factors.append(running)
            print(f'         {n} = {nth_fib}       {running}')

        for i in range (25, 35):
            get_fib_times(i)
        print('Results when dividing the time needed to find the n:th fib number with the time needed for finding the n-1:th')
        factor_qouitient_sum = 0 
        for i in range (1, 10):
            factor_qouitient_sum += (factors[i]/factors[i-1])
            print (factors[i]/factors[i-1])
        print(f'The avrage qoutient is {factor_qouitient_sum/9}.')
        print('Note: If main is called as a whole, more comupte is needed an all times become slower, \n' \
        'in addition the average factor between iterations becomes less accurate. \n ')
        print('We can support the claim that the time needed to run the function roughly scales with 1.618^n.')
    
        print(f'Since it takes {factors[-1]} seconds to find the 34th fibbonaci number')
        print(f'A reasonable assumption is that it would take {factors[-1]}*1.618^(50-34) to find the 50th fib number')
        print(f'Similarly, it would take {factors[-1]}*1.618^(100-34) to find the 100th fib number')

        time_for_50th_min = (factors[-1]*1.618**16)/60 ##use given value instead of calculated
        print(f'Which yields {round(time_for_50th_min, 2)} minutes for the 50th fibbonacci number')

        time_for_100th_sec = factors[-1]*1.618**66 ##use given value instead of calculated
        time_for_100th_years = time_for_100th_sec / (60 * 60 * 24 * 365)
        time_for_100th_years = round(time_for_100th_years, 2) ##round to two digits 
        print(f'Which yields {time_for_100th_years} years for the 100th fibbonacci number! \n')

    fib_test()
    ### code that analyzes fib_mem 

    def analyze_fib_mem():
        print('Analysis of fib_mem - a drastic improvement over fib')
        print('Fib number: ----------------------- Time:')
        start = time.perf_counter()
        fib100 = (fib_mem(100))
        running = time.perf_counter() - start
        print(f'100th = {fib100}       {round(running, 6)} seconds \n')

    analyze_fib_mem()


    def insertion_vs_merge():
        print('Comparing insertion and merge sort and how they handle large quantites.')
        print('Assuming both functions take 1 second to sort 1000 random numbers \n' \
        ', how long would would it take them to sort 10^6 and 10^9 numbers respectivley? \n')
        print('If we assume that the avrage case applies to both inputs, ' \
        'i.e. \n half the list must be checked, insertion scales by t_insert(n) = n(n+1)/4'
        '\n and merge by t_merge(n) = n*log(n). \n')

        ### 10^6 ###
        print('For 10^6 random numbers:')
        print('Time for insertion sort: t_insert(10^6)/t_insert(10^3) = (10^6 / 10^3)^2 = 10^6')
        print(f'Since we assume that t_insert(10^3) = 1 second: t_insert(10^6) = 10^6 seconds = {round((10**6)/(60*60*24),2)} days')
        print('Time for merge sort: t_merge(10^6)/t_merge(10^3) = (log(10^6)*10^6) / (log(10^3) * 10^3) = 2 * 10^3')
        print(f'Since we assume t_merge(10^3) = 1 second: t_merge(10^6) = 2000 seconds = {round(2000/60, 2)} minutes \n \n')
        
        ### 10^9 ###
        print('For 10^9 random numbers:')
        print('Time for insertion sort: t_insert(10^9)/t_insert(10^3) = (10^9 / 10^3)^2 = 10^12')              
        print(f'Since we assume that t_insert(10^3) = 1 second: t_insert(10^9) = 10^12 seconds = {round((10**12)/(60*60*24*365),2)} years')
        print('Time for merge sort: t_merge(10^9)/t_merge(10^3) = (log(10^9)*10^9) / (log(10^3) * 10^3) = 3 * 10^6')
        print(f'Since we assume t_merge(10^3) = 1 second: t_merge(10^9) = 3*10^6 seconds = {round((3*10**6)/(60*60*24), 2)} days. \n\n')

    insertion_vs_merge()

    def A_vs_B():
        print('Algorithm analysis, A vs B.')
        print('It takes algorithm A n seconds to solve a problem of size n. \n' \
        'It takes algorithm B c*n*log(n) seconds to solve the same problem, \n' \
        'where c is a constant.' \
        ' Since we know that B(10) = 1, we can find c.')
        print(f'1 = c * 10 *log(10) <=> c = 10*log(10) = 0.1')
        print('We thus have \n' \
        'A(n) = n \n' \
        'B(n) = 0.1*n*log(n)')
        ## find where A(n) = B(n)
        print('A(n) = B(n) <=> n = 0.1 * n * log(n) <=> 10 = log(n) <=> n = 10^10')
        print(f'A(n) is faster than B(n) IF n > 10^10')

    A_vs_B()

    print('\nBye!')

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the non-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
''' The number of required moves is proportional to (2^n) -1
Assuming each move takes one second to perform:
It takes 1125899906842623 seconds [or 35702051.84 years!] to complete the game with 50 tiles! '''
  ##calculation can be found in main under calculate_hanoi_50. 
  
  
  
  Exercise 9: Time for Fibonacci:
  ### from running main() ###
  ''' Thus we can support the claim that the time needed to run the function roughly scales with 1.618^n
Since it takes 1.385376800026279 seconds to find the 34th fibbonaci number
A reasonable assumption is that it would take 1.385376800026279*1.618^(50-34) to find the 50th fib number
Similarly, it would take 1.385376800026279*1.618^(100-34) to find the 100th fib number
Which yields 50.94 minutes for the 50th fibbonacci number
Which yields 2 724 855.3 years for the 100th fibbonacci number!'''
  ### note: the time for finding the fib numbers varies slightly each time i run the script due to diffrent background activity
  ### note: this error propages exponentially thus the diffrence between diffrent runs can be many years! 
  
  
  Exercise 10: Time for fib_mem:
  '''Analysis of time needed for the 50th and 100th fibbonacci number:
Fib number: ----------------------- Time:
100th = 354224848179261915075       0.000109 seconds'''
### calculations can be found in main under analyze_fib_mem
  
  
  Exercise 11: Comparison sorting methods:
  ### full code can be found in main under insertion_vs_merge:
  If we assume that the avrage case applies to both inputs, i.e. half the list must be checked, insertion scales by t_insert(n) = n(n+1)/4 and merge by t_merge(n) = n*log(n)
For 10^6 random numbers:
Time for insertion sort: t_insert(10^6)/t_insert(10^3) = (10^6 / 10^3)^2 = 10^6
Since we assume that t_insert(10^3) = 1 second: t_insert(10^6) = 10^6 seconds = 11.57 days
Time for merge sort: t_merge(10^6)/t_merge(10^3) = (log(10^6)*10^6) / (log(10^3) * 10^3) = 2 * 10^3
Since we assume t_merge(10^3) = 1 second: t_merge(10^6) = 2000 seconds = 33.33 minutes  

For 10^9 random numbers:
Time for insertion sort: t_insert(10^9)/t_insert(10^3) = (10^9 / 10^3)^2 = 10^12
Since we assume that t_insert(10^3) = 1 second: t_insert(10^9) = 10^12 seconds = 31709.79 years
Time for merge sort: t_merge(10^9)/t_merge(10^3) = (log(10^9)*10^9) / (log(10^3) * 10^3) = 3 * 10^6
Since we assume t_merge(10^3) = 1 second: t_merge(10^9) = 3*10^6 seconds = 34.72 days
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
Algorithm analysis, A vs B.
It takes algorithm A n seconds to solve a problem of size n. 
It takes algorithm B c*n*log(n) seconds to solve the same problem, 
where c is a constant. Since we know that B(10) = 1, we can find c.
1 = c * 10 *log(10) <=> c = 10*log(10) = 0.1
We thus have 
A(n) = n 
B(n) = 0.1*n*log(n)
A(n) = B(n) <=> n = 0.1 * n * log(n) <=> 10 = log(n) <=> n = 10^10
A(n) is faster than B(n) IF n > 10^10

Bye!
  
"""
