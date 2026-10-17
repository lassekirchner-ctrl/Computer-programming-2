##A8
#fix fib with memoization 
##see line in main:
#    FUNCTIONS_1['fib'] = lambda n: fib (n, memory) ### added line! 
#which fixes the issue 

#re-examn VT25

##A7
from tokenize import TokenError
import math
import io
import tokenize
import numpy as np


class TokenizeWrapper:
    def __init__(self, line):
        self.line = line
        self.tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        self.current = next(self.tokens)
        self.previous = 'START'

    def __str__(self):
        return self.current[0] + self.current[1]

    def get_current(self):
        if self.current[0] > 0:
            return self.current[1]
        else:
            return 'NO MORE TOKENS'

    def get_previous(self):
        return self.previous

    def next(self):
        # The return value is mainly intended for debugging purposes
        if self.has_next():
            self.previous = self.current[1]
            self.current = next(self.tokens)
            #print('next', self.current[0], self.current[1])
            return self.current
        else:
            return (0, 'EOS')

    def is_number(self):
        return self.current[0] == 2

    def is_name(self):
        return self.current[0] == 1

    def is_string(self):
        return self.current[0] == 3

    def is_newline(self):
        return self.current[0] == 4

    def is_comment(self):
        return self.current[0] == 55

    def is_at_end(self):
        return self.current[0] == 0 or self.current[0] == 4 or \
            self.current[1][0] == '#'  # self.current[0] == 55

    def has_next(self):
        return self.current[0] != 0 and self.current[0] != 4


def log(x):
    if x <= 0:
        raise EvaluationError(f'Illegal argument to log: {x}')
    return math.log(x)

import random 
def rand():
    return random.random()


#new group of functions
FUNCTIONS_0 = {'rand' : rand}


FUNCTIONS_1 = {  # Functions with a single argument
    'sin': math.sin,
    'cos': math.cos,
    'exp': math.exp,
    'log': log,
}

FUNCTIONS_N = {  # Functions with several arguments
    'sum': sum,
    'max': max
}

def arglist(wtok, variables):
    """ See syntax diagram for arglist"""
    if wtok.get_current() != '(':
        raise SyntaxError("Expected '(' after function name")
    wtok.next()
    args = []
    while True:
        a = assignment(wtok, variables)
        args.append(a)
        if wtok.get_current() == ')':
            wtok.next()
            break
        if wtok.get_current() != ',':
            raise SyntaxError('Incorrect argument list. Expected ","')
        wtok.next()
    return args

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    result = assignment(wtok, variables)
    while wtok.get_current() == ',':
        wtok.next()
        result = assignment(wtok, variables)
    if wtok.is_at_end() == False:
        raise SyntaxError('Expected comma or end of line')
    return result


def assignment(wtok, variables):
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected name after assignment operator")
        wtok.next()
    return result


def expression(wtok, variables):
    try:
        result = term(wtok, variables)
        while wtok.get_current() in ('+', '-'):
            if wtok.get_current() == '+':
                wtok.next()
                result = result + term(wtok, variables)
            else:
                wtok.next()
                result = result - term(wtok, variables)
        return result
    except (TypeError, ValueError) as te:
        raise EvaluationError(te)


def term(wtok, variables):
    result = factor(wtok, variables)
    while wtok.get_current() in ('*', '/'):
        op = wtok.get_current()
        wtok.next()
        if op == '*':
            result = result * factor(wtok, variables)
        else:
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
    return result


def parse(wtok, c, aux=''):  # Just for convenience
    if wtok.get_current() != c:
        raise SyntaxError(f"Expected '{c}'" + aux)
    wtok.next()


def factor(wtok, variables):
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        parse(wtok, ')', '')

    elif wtok.get_current() in FUNCTIONS_0:
        func = FUNCTIONS_0[wtok.get_current()]
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()
            if wtok.get_current() == ')':
                result = func()
                wtok.next()
            else:
                raise SyntaxError (f'Missing ")" after "()" ')
        else:
            raise SyntaxError (f"Missing '(' after {func}")
                


    elif wtok.get_current() in FUNCTIONS_1:
        func = FUNCTIONS_1[wtok.get_current()]
        wtok.next()
        if wtok.get_current() == '(':
            result = func(factor(wtok, variables))
        else:
            raise SyntaxError("Missing '(' after function name")
    elif wtok.get_current() in FUNCTIONS_N:
        func = wtok.get_current()
        wtok.next()
        args = arglist(wtok, variables)
        result = FUNCTIONS_N[func](args)

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(
                f"Undefined variable: '{wtok.get_current()}'")

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number, word or '('")
    return result


def vars_print(variables):
    for name, value in sorted(variables.items()):
        print(f"   {name:<5} : {value}")

def memory_print(memory):
    for name, value in sorted(memory.items()):
        print(f"   {name:<5} : {value}")


def main():

    print("Numerical calculator")
    variables = {"ans": "0.0", "PI": math.pi}##A8 tweak

    while True:
        line = input('\nInput: ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)
        if wtok.get_current() == 'vars':
            vars_print(variables)
        elif wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:

            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print(result)

            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"*** Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')


if __name__ == "__main__":
    pass
    #main()


#exam 2024 HT 

##A6
def A6(n:list):
    return list(filter(lambda x: x % 2 == 0, n))

def test_lst():
    numbers = [1 , 3 , 5]
    print (f" Even numbers : { A6 ( numbers )} " )
    numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 99]
    print (f" Even numbers : { A6 ( numbers )} " )

#test_lst()

##A7
def A7(n):
    n_lst = [x for x in range(n +1)] #list comp, py index starts at 0 
    return sum(list(map(lambda x: x**2, n_lst))) #map, lambda, sum
   


#print(A7(4))
    

##B3
def random_matrices(m,n,k):
    A = []
    for _ in range(m):
         res = [random.randrange(0, 10, 1) for _ in range(n)]
         A = A+[res]
    B = []
    for _ in range(n):
        res = [random.randrange(0, 10, 1) for _ in range(k)]
        B = B + [res]
    return A,B

import concurrent.futures as future
import numpy as np

    
#     return A * B

def multiplication(A,B):
    """B3: matrix multiplication"""
    num_rows_A, num_columns_A = np.shape(A)
    num_rows_B, num_columns_B = np.shape(B)
    n_p = min(num_columns_A, num_rows_B) # should both be n
    
    for col in num_columns_B:
        



def tets_multiplication():
    A , B = random_matrices (4 ,3 ,2)
    C = multiplication (A, B)
    print ( A )
    print ( B )
    print ( C )

tets_multiplication()