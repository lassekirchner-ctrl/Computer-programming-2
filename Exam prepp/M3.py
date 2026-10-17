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
    #main()
    pass


##B4
import concurrent.futures as future
import numpy as np 

def is_even_rounded(sub_frac):
    return np.sum(np.round(sub_frac) % 2 == 0)

def prob_even(n):
    n_p = 10 
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)
    frac = x/y
    chunck_size = int(n / n_p)
    chunks = []
    for i in range (n_p):
        start = i * chunck_size
        end = (i+1) * chunck_size 
        chunks.append(frac[start:end])

    with future.ProcessPoolExecutor(max_workers=n_p) as executor:
           results = list(executor.map(is_even_rounded, chunks))
    total_events = sum(results)
    return total_events / n


if __name__ == "__main__":
    pass
    #print(prob_even(10**8))

#tenta 2024 HT 
##A4



class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def append(self, x):
        if self.first is None:
            self.first = LinkedList.Node(x, None )
            return 1
        lenght = 2 #only gets triggered when if dosent, means we have at least len = 2
        current = self.first 
        while current.succ is not None:
            lenght += 1
            current = current.succ 
        current.succ = LinkedList.Node(x, None)
        return lenght
       
        
def test_append():
    lst = LinkedList ()
    print ( lst )
    for i in [5 ,2 ,10 ,5]:
        l = lst . append ( i )
        print ( lst , l )

#test_append()

class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.count = 1  # For use in task B2

        def __str__(self):
            return f'({self.key}, {self.count})'

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self
            if self.right:
                yield from self.right

    def __init__(self, init=None):
        self.root = None
        if init:
            for x in init:
                self.insert(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        return '<' + ', '.join([str(x.key) for x in self]) + '>'

    def __repr__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def insert(self, key):
        """ Standard binary search tree insertion, not a part of B2
        """
        def insert(key, r):
            if r is None:
                return BST.Node(key)
            elif key < r.key:
                r.left = insert(key, r.left)
            elif key > r.key:
                r.right = insert(key, r.right)
            else:
                pass # Already there. Do nothing.
            return r

        self.root = insert(key, self.root)

    def sum_level(self, level):
        """ A5: Returns the sum of the key values of the node on level """

        def _sum(r, lvl):
            if r is None:
                return 0
            if lvl == 0:
                return r.key 
            return _sum(r.left, lvl -1) + _sum(r.right, lvl-1)
        
        return _sum(self.root, level)

    def B2_insert(self, key):
        def _insert(key, r):
            if r is None:
                return BST.Node(key)
            elif key < r.key:
                r.left = _insert(key, r.left)
            elif key > r.key:
                r.right = _insert(key, r.right)
            else:
                return r 

            r.count = 1 + (r.left.count if r.left is not None else 0) + (r.right.count if r.right else 0)
            return r 

        self.root = _insert(key, self.root)


def test_B2insert():
    inserts = (10 , 5 , 1 , 7 , 20 , 30 , 15 , 17 , 12 , 2)
    print (f'Inserted keys : { inserts } ')
    tree = BST ()
    for x in inserts :
        tree . B2_insert( x )
        print (f' After inserting { x }: { repr ( tree )} ')

test_B2insert()


##A5
def test_sum_level():
    inserts = (5 , 8 , 1 , 3 , 7 , 2 , 6 , 9)
    print(f' Inserted keys : { inserts } ')
    tree = BST ( inserts )
    print ( ' Level Sum of keys ')
    for level in (0 , 1 , 2 , 3 , 4):
        result = tree . sum_level ( level )
        print (f'{ level :3d} { result :10d} ')

#test_sum_level()