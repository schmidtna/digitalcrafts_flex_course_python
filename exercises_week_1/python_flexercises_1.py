# Take basic input ex 1
def name_input():
    user_name = input("Type your name: ")
    print("Hello, " + user_name + "!")

# name_input()

# Take input and count it ex 2

def name_count():
    user_name = input("Type your name: ")
    user_name = user_name.upper()
    print("Hello, " + user_name + "!")
    print("Your name has " + str(len(user_name)) + " characters in it!")

# name_count()

# madlib ex 3

def madlib():
    print("Fill in the blanks below :\n___(name)___'s favorite subject in school is ___(subject)___")
    user_name = input("Type a name :")
    user_subject = input("Type a school subject :")
    print("{}'s favotite subject in school is {}.".format(user_name, user_subject))
    
madlib()


