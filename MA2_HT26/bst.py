""" bst.py

Student: Lars Kirchner
E-mail: lasse.kirchner@gmail.com
Reviewed by: Andreas Michael
Review date: 22-09-26
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains_old(self, k): # given function
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None


    # def contains(self, k) # Exc8: write recursive contains
    def contains(self, k):
    
        def recurs(n):
            if n == None:
                return False  
            # if n.key == k:
            #     return True 
            else:
                if k < n.key:
                    n = n.left 
                    return recurs(n)
                elif k > n.key:
                    n = n.right 
                    return recurs(n)
                else:
                    return True

        return recurs (self.root)


    def size(self): # counts the number of nodes 
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#
    # Exc9
    def height(self):
        return self._height(self.root)

    def _height(self, r):
        if r == None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right)) 

    # Exc10
    def __str__(self):   
        res = []
        for x in self:
            if self.root == None:
                return '<>' 
            else:
                res.append(str(x))
        return '<'+ ', '.join(res)+'>'
        

    # Exc11  
    def to_list(self):
        res = []
        for x in self: 
            if self.root == None:
                return res
            else:
                res.append(x)
        return res

        # Complexity of to_list:
        '''Complexity should be linear, since each element is 
        iterated over and direcrtly inserted into the result'''

    # Exc12
    def to_LinkedList_old(self):    
        res = LinkedList()
        reg_list = self.to_list()
        for item in reg_list:
            res.insert(item)
        return res

    ##is n^2 since insert is called and for item...

    def to_LinkedList(self):    
        res = LinkedList()

        first_item = True
        last = None

        for item in self:
            new_node = res.Node(item, None)

            if first_item == True:
                res.first = new_node
                first_item = False
            
            else:
                last.succ = new_node
            last = new_node
             
        return res 
                         
        # Complexity of to_LinkedList:
        ## since this approach is built on the same logic as copy, it should be o(n) aswell! 


    def remove(self, key):
        self.root = self._remove(self.root, key)

    # Exc13
    def _remove(self, r, k):      
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k) 
        elif k > r.key:
            # r.right =  right subtree with k removed
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
                smallest = r.right #we start to the right, and then move left as long as its not none
                while smallest.left != None: 
                    smallest = smallest.left
                r.key = smallest.key #sets the key 
            r.right = self._remove(r.right, smallest.key) ##removes old duplicate
        return r  # Remember this! It applies to some of the cases above


    '''Exercise 14: Complexity of search
        In a binary search tree with n nodes and height h, what is the complexity in
        the following scenarios:
         Worst case of successful search
         Worst case of failed search
        Later voluntary exercises will cover more theory regarding the complexity of
        binary tree operations'''
    
def ex14():
        print('What is the complexity for a search in a binary tree with n nodes and height h? \n')
        print(f'Scenario 1: Worst case successful search \n')
        print(f'Scenario 2: Worst case failed search \n')
        print('Examining scenario 1: the worst case is that the value \n' \
        'is a leaf, meaning we have to check h levels')
        print('The complexity of the serach should be linear, \n ' \
        'since the number of steps is directly proportional to h')

        print('For scenario 2, test complexity should be identical, \n' \
        'since going to the end of a branch items occurs in both cases +\n '
        'whereafter the search is finished or failed.')

### test code for height 
import unittest
class TestBST(unittest.TestCase): ##needs to be a class for unittest
    def test_height(self): ## didnt relaize there was given test code...
        # no nodes
        bst = BST()
        self.assertEqual(bst.height(), 0,
                        'ERROR: An empty tree should have height 0.')

        #one nide
        bst.insert(5)
        self.assertEqual(bst.height(), 1,
                        'ERROR: A tree with 1 node should have height 1.')
        
        #two nodes
        bst.insert(4)
        self.assertEqual(bst.height(), 2,
                        'ERROR: A tree with 2 nodes should have height 2.')

        ##three nodes 
        bst.insert(3)
        self.assertEqual(bst.height(), 3,
                        'ERROR: A tree with nodes 5, 4, 3 should have height 3.')

        ## tests three nodes, height
        bst = BST()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.height(), 2,
                        'Error: A tree with root 2 and kids 1 and 3 should have height 2')

    def test_str(self): ## didnt relaize there was given test code...
        bst = BST()
        ## empty string
        self.assertEqual(bst.__str__(), '<>',
                        'FAILED')

        ##one item
        bst.insert(1)
        self.assertEqual(bst.__str__(), '<1>',
                                'FAILED')

        # multiple 
        bst.insert(2)
        self.assertEqual(bst.__str__(), '<1, 2>',
                                        'FAILED')

        ##non ordered sample
        bst = BST()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.__str__(), '<1, 2, 3>')

    def test_to_list(self): ## didnt relaize there was given test code...
        bst = BST()

        #test empty
        self.assertEqual(bst.to_list(), [],
                                'ERROR, empty tree should yield zero!')

        #test 'in order'
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        self.assertEqual(bst.to_list(), [1, 2, 3],
                        'ERROR')

        bst= BST()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(-5)
        self.assertEqual(bst.to_list(), [-5, 1, 2, 3],
                        'ERROR')


    def test_remove(self):

        # Example 1: remove a leaf
        bst = BST()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)

        bst.remove(3)

        self.assertEqual(
            bst.to_list(),
            [5, 7],
            'FAILED: Removing 3 should leave [5, 7].')


        # Example 2: remove a node with two children
        bst = BST()
        bst.insert(5)
        bst.insert(3)
        bst.insert(8)
        bst.insert(6)
        bst.insert(9)

        bst.remove(8)

        self.assertEqual(
            bst.to_list(),
            [3, 5, 6, 9],
            'FAILED: Removing 8 should leave [3, 5, 6, 9].')
        

def main(): ##kinda wierd first try, probably should use unittest in the future. 
    def test_contains():
        t = BST()
        for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
            t.insert(x)
        t.print()
        print()

        print('size  : ', t.size())
        for k in [0, 1, 2, 5, 9]:
            print(f"contains({k}): {t.contains(k)}")

    test_contains()



if __name__ == "__main__":
    main()
    #ex14()
    unittest.main()
    


"""
Exc14: In a binary search tree with n nodes and height h, what is the complexity in the
following scenarios:
=============================="""
'''

Scenario 1: Worst case successful search 

Scenario 2: Worst case failed search 

Examining scenario 1: the worst case is that the value 
is a leaf, meaning we have to check h levels
The complexity of the serach should be linear, 
 since the number of steps is directly proportional to h
For scenario 2, test complexity should be identical, 
since going to the end of a branch items occurs in both cases +
 whereafter the search is finished or failed.

'''