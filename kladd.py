def largest(a: list):
    lenght_input_list = len(a)

    #find a ground value, note that the first element in a might be a list!
    if type(a[0]) == list : #handles the case if a[0] is a list
        res = largest(a[0])
    else: 
        res = a[0] # if a[0] is a int

    # actual function for finding the largest value

    for i in range (0, lenght_input_list):
        if type(a[i]) == list:
            possible_res = largest(a[i])
            if possible_res > res:
                res = possible_res
        else:
            if a[i]> res:
                res = a[i] 
    return res

test1 = [1, 2, 3, 4, 5]
print(largest(test1))

test2 = [5, 6, [1, -1]]
print(largest(test2))
test3 = [[1, -1], [3, 4, 5, 7]]
print(largest(test3))

test4 = [[[[1, 2], [3, 4, 5]], [6, 7], 8]] 
print(largest(test4))

