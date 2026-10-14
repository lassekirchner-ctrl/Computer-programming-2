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
test_base11()


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
