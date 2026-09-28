""" linked_list.py

Student: Lars Kirchner
Mail: lasse.kirchner@gmail.com
Reviewed by: Andreas Michael
Review date: 22-09-26
"""

##to move a bunch of selected rows of code inwards, i.e. decrese indent: ctrl+backslash (to the left of the backspace)
class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self): # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __contains__(self, x):# Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    # Exc1
    def length(self): 
        num_nodes = 0
        f = self.first # must be before loops? => yes! 
        if self.first is None:
            return 0
        
        else:    
            while f != None: ##use != to better understand, i know its uncessary
                num_nodes += 1 
                f = f.succ #moves to the next node??? => yes! 
        return num_nodes

        '''Exercise 2: Method remove_last
        Write a method which removes the last node from the list. The method should
        return the value in the removed node.
        If the list is empty, a ValueError should be raised. (ValueError is a standard
        exception class in Python.)'''
        # Exc2
    def remove_last(self):     
        f = self.first
        removed = 0
        if f is None:
            raise ValueError
        elif f.succ == None:
            removed = f.data
            self.first = None
            return removed
        else:
            while f.succ.succ != None:
                f = f.succ
                #print("f is currently:", f.data)
            removed = f.succ.data ## the data part is important, without we just get identify the node and note the value
            f.succ = None
        return removed
    '''Write a method remove(self, x) which deletes the first node containing x as
data. If the method finds a node with this content, it should return True else
False. Use iteration here. We will discuss how to do this recursively soon. Make sure
that the method works even if the element to be removed is currently the first
or the last element of the list'''

    # Exc3
    def remove(self, x):         
        f = self.first 
        if self.length() == 0: #handles the case where f is empty and dosent point?
            return False
        elif f.data == x: # is the data-call correct??? => yes 
            self.first = f.succ
            return True 
        else:
            for i in range (0, self.length()):
                if f.succ == None:
                    return False
                elif f.succ.data == x:
                    f.succ = f.succ.succ
                    return True  
                else:
                    f = f.succ
            return False 

    ### EX4
    def to_list(self):        
        py_list = []

        def recurs(node): ### use nodes instead of f = self.first to avoid desctruction
            if node == None:
             return py_list 
            else:
                if node.succ == None:
                    py_list.append(node.data)
                    return py_list
                else:
                    py_list.append(node.data)
                return py_list + recurs(node.succ)   

        recurs(self.first)
        return py_list
        
    # Exc5
    #def __str__(self):    
        result = []
        separator = ', ' 
        for item in self:
            result.append(str(item))
        string = separator.join(result)
        string = '(' + string + ' )'
        return string

    def __str__(self):    
            result = []
            separator = ', ' 
            for item in self:
                result.append(str(item))
            return '(' + separator.join(result) + ')'
      

    def copy_given(self):
        result = LinkedList()
        for x in self: 
            result.insert(x)
        return result
        # Complexity for this implementation:
        '''The complexity for the given copy should be quadratic in the worst case since the 
        loop walks thorugh all items, n, and insert might have to serach all n items to find
        the correct place to insert, thus we have n*n'''

    # Exc6, should be more efficient
    def copy(self):
        result = LinkedList()
        ### copy list in order to avoid seraching using insert(). 

        if self.first == None:
            return result

        current = self.first 
        # create first node in res
        result.first = result.Node(current.data, None)

        last = result.first 
        current = current.succ #step in the original list

        while current != None:
            last.succ = result.Node(current.data, None)
            last = last.succ #step in the new list 
            current = current.succ # step in the old list
        return result
    # Complexity for this implementation:
    ''' The complexity should be n since we look at each node once, 
    and create each onde once. The code dosent call insert for each value, 
    which means that its linear and not n^2 since values are copied directly,
    and we know that they are in order! '''


    #ex7 - person class in linkedlist
    # sort via pnr instead of name! 
class Person:
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __eq__(self, other ):
        return self.pnr == other.pnr 

    def __lt__(self, other):
        return self.pnr < other.pnr

    def __le__(self, other):
        return self.pnr <= other.pnr


def main():
    print('Tests if dunder methods are implemented correctly.')
    plist = LinkedList()

    p = Person('Erik', '20021231')
    q = Person('Lars', '20041207')
    r = Person('Erik_twin', '20021231')

    plist.insert(p)
    plist.insert(q)
    plist.insert(r)

    plist.print()

    # test if my dunders work
    assert p < q
    assert p <= q
    assert p == r

    assert not q < p
    assert not q <= p
    assert not p == q

    print("OK!")


if __name__ == '__main__':
    main()