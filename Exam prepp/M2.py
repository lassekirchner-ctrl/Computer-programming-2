class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current is not None:
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

    
    def copy_new(self):
        if self.first == None:
            return None
        else:
            new_lst = LinkedList()
            for i in self:
                new_lst.insert(i)
            return new_lst


def Merge(ll1,ll2): ##Exercise B2
    if ll1.first is None:
        return ll2.copy_new()
    elif ll2.first is None:
        return ll1.copy_new()
    else:
        new_lst = LinkedList()

        curr_ll1 = ll1.first 
        curr_ll2 = ll2.first

        if curr_ll1.data > curr_ll2.data:
            new_lst.first = LinkedList.Node(curr_ll2.data)
            curr_ll2 = curr_ll2.succ
        else:
            new_lst.first = LinkedList.Node(curr_ll1.data)
            curr_ll1 = curr_ll1.succ

        r = new_lst.first

        while curr_ll1 is not None and curr_ll2 is not None:  
            if curr_ll1.data > curr_ll2.data:
                r.succ = LinkedList.Node(curr_ll2.data)
                curr_ll2 = curr_ll2.succ
            else:
                r.succ = LinkedList.Node(curr_ll1.data)
                curr_ll1 = curr_ll1.succ 
            r = r.succ

        while curr_ll1 is not None:
            r.succ = LinkedList.Node(curr_ll1.data)
            curr_ll1 = curr_ll1.succ
            r = r.succ

        while curr_ll2 is not None:
            r.succ = LinkedList.Node(curr_ll2.data)
            curr_ll2 = curr_ll2.succ
            r = r.succ        

    return new_lst

def main():
    # print("Test A3:")
    # queue = Queue()
    # for x in ["A", "B", "C", "D", "E"]:
    #     queue.Enqueue(x)
    # print(queue)
    # for _ in range(5):
    #     queue.Dequeue()
    #     print(queue)
    # print("Test A4:")
    # X = [ [5, 8, 3, 7, 2, 6, 9], [4, 1, 3, 6, 7, 5, 8], []]
    # for x in X:
    #     bst = BST()
    #     for i in x:
    #         bst.insert(i)
    #     m = bst.max()
    #     print(m)
    print("Test B2:")
    X = [[1,3,6,7], [], []]
    Y = [[0,2,8,9], [1,2,3], []]
    for lst1, lst2 in zip(X,Y):
        ll1, ll2 = LinkedList(), LinkedList()
        for x in lst1:
            ll1.insert(x)
        for x in lst2:
            ll2.insert(x)
        ll3 = Merge(ll1,ll2)
        print(ll3)
    # print("Test B3:")
    # print("The complexity of the method in B3 is ?")
    # X = [[0], [1,2],[1,2,3],[1,2,3,5],[1,2,3,5,8], list(range(100))] #
    # for lst in X:
    #     ll = LinkedList()
    #     for x in lst:
    #         ll.insert(x)
    #     print(ll.middle(), lst[(len(lst))//2])
if __name__ == '__main__':
    main()


