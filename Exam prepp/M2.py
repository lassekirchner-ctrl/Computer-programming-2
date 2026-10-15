##ordinary exam VT 2025

##A3
class Queue:

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

    def Enqueue(self, x):
        if self.first:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = Queue.Node(x, None)
        else:
            self.first = Queue.Node(x, None)

    #in a Class Queue with a subclass node
    def Remove_frst(self): ##Exercise A3
        if self.first is not None :
            self.first = self.first.succ

    
def test_queue():
    queue = Queue ()
    for x in [ " A " , " B " , " C " , " D " , " E " ]:
        queue.Enqueue ( x )
        print ( queue )
        for _ in range (5):
            queue.Dequeue ()
            print (queue)

#test_queue()


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right
    def __init__(self):
        self.root = None
    def __iter__(self):
        if self.root:
            yield from self.root
    def __str__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'
    def insert(self, key):
        def _insert(r, key):
            if r is None:
                return self.Node(key)
            elif key < r.key:
                r.left = _insert(r.left, key)
            elif key > r.key:
                r.right = _insert(r.right, key)
            else:
                pass
            return r
        self.root = _insert(self.root, key)
    def max(self): ##Exercise A4
        if self.root == None:
            return None
        else:
            r = self.root
            while r.right is not None :
                r = r.right
            return r.key 


def test_max():
    X = [ [5 , 8 , 3 , 7 , 2 , 6 , 9] , [4 , 1 , 3 , 6 , 7 , 5 , 8] , []]
    for x in X :
        bst = BST ()
        for i in x:
            bst.insert(i)
        m = bst.max()
        print (m) 

#test_max()

##B2 and B3
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

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = LinkedList.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = LinkedList.Node(x, f.succ)

    def copy(self): #can be used in Exercise B2
        result = LinkedList()
        for i in self:
            result.insert(i)
        return result
    
    def middle(self): ##Exercise B3
        lead = trail = self.first 
        if lead is None:
            return None
        else:
            while lead is not None and lead.succ is not None:
                lead = lead.succ.succ
                trail = trail.succ
        return trail.data
    #complexity should be n since it the lenght doublees, we need to visit twice as many nodes. 

def test_middle():
    X = [[0] , [1 ,2] ,[1 ,2 ,3] ,[1 ,2 ,3 ,5] ,[1 ,2 ,3 ,5 ,8] , list ( range (100))]
    for lst in X :
        ll = LinkedList ()
        for x in lst :
            ll.insert ( x )
        print ( ll . middle () , lst [( len ( lst ))//2])

#test_middle()

def Merge(ll1,ll2): ##Exercise B2
    x1 = ll1.first
    x2 = ll2.first

    if x1 is None:
        result = ll2.copy() 
        return result
    elif x2 is None:
        result = ll1.copy()
        return result
    else:
        result = LinkedList()
        if x1.data < x2.data:
            result.first = LinkedList.Node(x1.data)
            x1 = x1.succ
        else:
            result.first = LinkedList.Node(x2.data)
            x2 = x2.succ 
        r = result.first

        while x1 is not None and x2 is not None:
            if x1.data < x2.data:
                r.succ = LinkedList.Node(x1.data)
                x1 = x1.succ
            else:
                r.succ = LinkedList.Node(x2.data)
                x2 = x2.succ 
            r = r.succ 

        while x1 is not None:
            r.succ = LinkedList.Node(x1.data)
            x1 = x1.succ
            r = r.succ

        while x2 is not None:
            r.succ = LinkedList.Node(x2.data)
            x2 = x2.succ
            r = r.succ

        return result

def test_merge():
    X = [[1 ,3 ,6 ,7] , [] , []]
    Y = [[0 ,2 ,8 ,9] , [1 ,2 ,3] , []]
    for lst1 , lst2 in zip (X , Y ):
        ll1 , ll2 = LinkedList () , LinkedList ()
        for x in lst1 :
            ll1 . insert ( x )
        for x in lst2 :
            ll2 . insert ( x )
        ll3 = Merge ( ll1 , ll2 )
        print ( ll3 )

#test_merge()



## re-exam VT25

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def insert(self, key):
        def _insert(r, key):
            if r is None:
                return self.Node(key)
            elif key < r.key:
                r.left = _insert(r.left, key)
            elif key > r.key:
                r.right = _insert(r.right, key)
            else:
                pass  # Already there
            return r

        self.root = _insert(self.root, key)

    def min(self): ##Exercise A3
        if self.root == None:
            return None
        else:
            r = self.root
            while r.left is not None:
                r = r.left 
            return r.key 

def test_min():
    X = [[5 , 8 , 3 , 7 , 2 , 6 , 9] , [4 , 1 , 3 , 6 , 7 , 5 , 8] , []]
    for x in X :
        bst = BST ()
        for i in x :
            bst.insert ( i )
        m = bst . min ()
        print(m) 

#test_min()

##A4
class Stack:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None
        self.Fiba = 1
        self.Fibb = 1
    def __iter__(self): #reverses the order? 
        current = self.first
        while current: #is not None 
            yield current.data
            current = current.succ
    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def Push(self, x):
        self.first = Stack.Node(x, self.first)

    def Pop(self): ##Exercise A3
        if self.first is not None:
            self.first = self.first.succ 

def test_pop():
    stack = Stack ()
    # E is added last and thus is removed first
    for x in [ " A " , " B " , " C " , " D " , " E " ]:
        stack . Push ( x )
    print ( stack )
    for _ in range (6):
       stack . Pop ()
       print ( stack )

#test_pop()

##B2
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

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = LinkedList.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = LinkedList.Node(x, f.succ)

    def middle(self): ##Exercise B2
        lead = trail = self.first 
        if lead is None:
            return None
        while lead is not None and lead.succ is not None:
            lead = lead.succ.succ 
            trail = trail.succ
        return trail.data 





def test_middle():
    X = [[0] , [1 ,2] ,[1 ,2 ,3] ,[1 ,2 ,3 ,5] ,[1 ,2 ,3 ,5 ,8] , list ( range (100))]
    for lst in X :
        ll = LinkedList ()
    for x in lst :
        ll . insert ( x )
    print ( ll . middle () , lst [( len ( lst ))//2])

#test_middle()

##B3
class Fib: #Exercise B3. Write Class Lucas below Class Fib.
    def __init__(self):
        self.a = 1
        self.b = 1
    def __str__(self):
        return ("I represent an infinite sequence!")

    def next(self):
        print(str(self.a), end=" ")
        self.a, self.b =  self.b, self.a + self.b 
        ##neds to be a tuple assignment
class Lucas(Fib):
    def __init__(self):
        self.a = 2
        self.b = 1

def test_lucas():
    F = Fib ()
    for _ in range (15):
        F.next()
    print ( " " )
    L = Lucas ()
    for _ in range (15):
        L.next()
    print ( " " )
    print ( L )

#test_lucas()


#exam 2024 HT

##A3 calculator question


