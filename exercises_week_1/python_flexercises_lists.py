# sum a list ex 1

# number_list = [1, 2, 3, 4, 5]
# print(sum(number_list))

# print largest ex 2, 3

def list_sorting():
    mylist = [ 5, 6, 1, 7, 3, 9]
    mylist.sort()
    print(mylist.pop())
    print(mylist.pop(0))

# list_sorting()

# list scanning ex 4, 5, 6

def scanning_list():
    evens_list = []
    above_zero = []
    mylist = [ 5, 6, 1, 7, 3, 9, 0, -3, -4, -1, -6, -8]
    for i in mylist:
        if i % 2 == 0:
            evens_list.append(i)
        elif i > 0:
            above_zero.append(i)

    print(evens_list)
    print(above_zero)

# scanning_list()

# multiply a list ex 7

def factor_multi():
    mult_factor = 4
    start_list = [1, 2, 3, 4, 5]
    multi_list = []
    for i in start_list:
        multi_list.append(i * mult_factor)

    print(multi_list)

# factor_multi() ex 8
def list_multi():
    numlist_1 = [1, 2, 3]
    numlist_2 = [4, 5, 6]
    cross_multi = [numlist_1 * numlist_2 for numlist_1, numlist_2 in zip(numlist_1, numlist_2)]

    print(cross_multi)

# list_multi()

# matrix addition ex 9, 10
import numpy as np

def matrix_add():
    matrix1 = np.matrix([[2, -2, 7, 11], [4, 6, 5, 101]])
    matrix2 = np.matrix([[3, 4, 6, 18], [5, 6, 30, 7]])
    
    print(matrix1 + matrix2)

# matrix_add()

# setting sets ex 11

def cleanup():
    stuffs = ["cheese", "fish", "more", "cheese", "more", "are", "more", "funky"]
    filter_bucket = set(stuffs)
    print(filter_bucket)

# cleanup()

# bonus ex 12

def matrix_multi():
    matrix1 = np.matrix([[2, 3], [6, 7]])
    matrix2 = np.matrix([[6, 7], [2, 3]])
    
    print(matrix1 * matrix2)

# matrix_multi()
