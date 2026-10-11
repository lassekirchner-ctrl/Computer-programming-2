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

test_pop()