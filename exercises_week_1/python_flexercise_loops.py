# ex 1

def prnt_rng():
    for i in range(1, 11):
        print(i)

# prnt_rng()

# ex 2

def step_count():

       
    starter = input("Enter a number to start counting from : ")
    ender = input("Enter the last possible number to count to : ")

    starter = int(starter)
    ender = int(ender)

    for i in range(starter, (ender + 1)):
        print(i)

# step_count()

# ex 3

def odd_counter():

    for i in range(1, 11):
        if i % 2 != 0:
            print(i)

# odd_counter()

