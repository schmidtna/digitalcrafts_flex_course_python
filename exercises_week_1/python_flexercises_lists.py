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

# list scanning ex 4, 5

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

scanning_list()
