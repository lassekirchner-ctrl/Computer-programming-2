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
'this means that the method is n**2 overall. A regular implementation could likely be n**1')
