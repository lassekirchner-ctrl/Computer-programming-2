import math 


# Ordinary examn 2025 VT 
#A1 Write a function base3(x) using recursion that returns the number x expressed in the base 3
def base3(x : int):
    if x < 0: #handels negative inputs 
        return '-' + base3(-x)
    if x == 0:
        return '0' 
    elif x == 1:
        return '1'
    elif x == 2:
        return '2'
    elif x > 2:
        return base3(x // 3) + str((x % 3))


def test_base3():
    for x in [3, 6, 20, 27, 28, 52]:
        print(base3(x), end = ' ')

#test_base3()

#notes: remember the edge cases and that no result  = '' is needed
#also, the acutal caluations are only 1 row!


##A2
#dont use // or %, se digit_sum instead! 
def digit_sum(x):
        """ Computes and returns the sum of the digits
        """
        if x < 10:
            return x
        else:
            result  = 0
            y = str(x)
            for i in y:
                result += int(i)
            return result
def divisible9(x):
    if x < 0:
        return divisible9(-x) 
    elif x == 9 or x == 0: # zero techinically devisible by 9
        return True 
    elif x < 10:
        return False 
    else:
        return divisible9(digit_sum(x)) 
    
# print(type(digit_sum(18) / 3))
# print(digit_sum(18))
# print(18/3)


def test_div_9():
    for x in [9, 18, 9000, 25689, 24606]:
        print(divisible9(x))


##B1 tower of hanoi
class TowerHanoi:
    def bricklek(self):
        def _bricklek(k, start = 0, goal = 1, help = 1):
            if k == 0:
                return []
            else:
                return _bricklek(k-1, start, help, goal) + \
                [(start, goal)] + _bricklek(k-1, help, goal, start)

        return _bricklek(self.n)

    def __init__ (self, n):
        self.n = n
        self.ListOfList = [list(range(n)), [], []]
        self._time = 0
        self.instructions = self.bricklek()

    def __str__(self):
        stacks = ['Start', 'Help', 'Goal']
        repr = 'step' + str(self._time) + '\n'
        for s, l in zip(stacks, self.ListOfList):
            repr += s + ':' + '+' +'\n'
            for n in l:
                repr += '*' *(n+1) + '\n'
        return repr 

    def step(self):
        curr = self.instructions[self._time]
        out = curr[0]
        _in = curr[1]
        element = self.ListOfList[out][0]
        self.ListOfList[out] = self.ListOfList[out][1:]
        self.ListOfList[_in].insert(0, element)
        self._time = self._time + 1 



def test_hanoi():
    TH = TowerHanoi (3)
    for _ in range (5):
        TH . step ()
        print ( TH )

#test_hanoi()


##B1
def base11(x):
    def inner(x):
        if x < 10:
            return str(x)
        else:
            return 'A'
    if x < 0:
        return '-' + base11(-x)
    elif x < 11:
        return inner(x)
    else:
        return base11(x // 11) + inner((x % 11))

def test_base11():
    for x in [9 , 44 , 120 , 1000 ,1111]:   
        print ( base11 ( x ) , end = " " )
#test_base11()


##re-exam VT 2025

#test_div_9()
def sum_prime(x): ##Exercise A1
    def is_prime(n):##given funktion
        if n <= 1:
            return False
        else:
            is_prime = True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            return is_prime
    if x <= 1:
        return 0
    if is_prime(x) == True:
        return x + sum_prime(x - 1)
    else:
        return sum_prime(x-1)

def test_sum_prime():
    for x in [4, 5, 6, 7, 100]:
        print(sum_prime(x), end = ' ')

#test_sum_prime()

##A2
#print('Using recorsion, we make the problem more complicated than it' \
'has to be. we call is prime for n numbers, and then also call sum prime' \
'this means that the method is n**2 overall. A regular implementation could likely be n**1'


#exam 2024 HT

def A1(n): 
    """ A1: complete the function """
    memory = {}
    def A1_inner(n):

        if n not in memory:
            if n < 4:
                memory [n] = 1
                return 1
            else:
                memory [n] = 2*A1_inner(n-1) - 4*A1_inner(n-2) + 3*A1_inner(n-3) -A1_inner(n-4)
                return memory [n]
        else:
            return memory[n]
    return A1_inner(n)

    
def A2_old(input_string): ##works! but dosent recurse
    while input_string[0] == input_string[-1]:
        if len(input_string) == 1 or len(input_string) == 2:
            return True 
        input_string = input_string[1: (len(input_string)-1)]
    return False 

def A2(input_string):  
    if len(input_string) == 0:
        return False #we need a word to check of palindrom
    if input_string[0] == input_string[-1]:
        if len(input_string) == 1 or len(input_string) == 2:
            return True 
        return A2(input_string[1: (len(input_string)-1)])
    return False 

def test_A2():
    print(A2('madam'))
    print(A2('knas'))
    print(A2('racecar'))
    print(A2('mmmmmmmbmmmmmmmmmmmmmmmmmmmmmmmmmmm'))
    print(A2('dammad'))

#test_A2()

def B1(lst):
    lst_even = []
    lst_odd = []

    def B1_inner(lst):
        if len(lst) == 0:
            return lst_even, lst_odd
        if len(lst) == 1:
            lst_even.append(lst[0])
            return lst_even, lst_odd
        else: # len(lst) >= 2
            lst_even.append(lst[0])
            lst_odd.append(lst[1])
            return B1_inner(lst[2:])
    B1_inner(lst)
    return lst_even, lst_odd


def test_B1():
    lists = ([],
             [0],
             [0, 1],
             [0, 1, 2],
             [0, 1, 2, 3],
             [0, 1, 2, 3, 4]
             )
    for lst in lists:
       print(f'{str(lst):15s} \t {B1(lst)}')

test_B1()