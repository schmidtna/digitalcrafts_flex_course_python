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
# if __name__ == "__main__":
# odd_counter()

# ex 4

def star_square():
    height = 5
    for i in range(height + 1):
        print("*" * height)

# star_square()

# ex 5

def input_square():
    height = int(input("enter square size : ")) 
    for i in range(height + 1):
        print("*" * height)

# input_square()

# ex 6

def input_box():
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    cappers = ("*" * width)
    space_fill = (" " * (width - 2))

    print(cappers)
    
    for i in range(height - 2):
        print(space_fill.center(width, "*"))
    
    print(cappers)

# input_box()

# ex 7, 8

def staramid():
   
    height = int(input("How Tall? "))
   
    for i in range(1, height, 2):
        star_count = ("*" * i)
        print(star_count.center(height, " "))
    
    
# staramid()

# ex 9

def multi_table(tab_number):

    for i in range(1, 11):
        print("{} X {} = {}".format(tab_number, i, tab_number * i))

# multi_table(1)
# multi_table(2)
# multi_table(3)
# multi_table(4)
# multi_table(5)
# multi_table(6)
# multi_table(7)
# multi_table(8)
# multi_table(9)
# multi_table(10)


    


