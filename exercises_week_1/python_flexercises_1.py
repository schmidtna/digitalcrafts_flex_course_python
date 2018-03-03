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

# madlib()

# Day of week ex 4, 5

def days_of_week():
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_number = -1
    print("Enter a number (0-6) to pick a day, 0 = Sunday.")
    while day_number not in range(0, 7):
        day_number = int(input("Enter your number :"))
        if day_number in range(1, 6):
            print("You chose {} go to work!".format(days_list[day_number]))
            break
        elif day_number == 0 or day_number == 6:
            print("You chose {}, sleep in!".format(days_list[day_number]))
            break
        else:
            print("Sorry, your input was invalid, only use numbers 0-6")

# days_of_week()

# Clecsius to Faren ex 6

def temp_converter():
    celc_input = int(input("Enter the temperature in Celcius :"))
    faren_temp = ((celc_input * 1.8) + 32)
    print("The temperature in Farenheit is {}".format(faren_temp))

# temp_converter()
    
# Tip calculator ex 7, 8


def tip_calc():
    bill_cost = float(input("What was your total bill amount? $"))
    levels = {
        'good': bill_cost * .2,
        'fair': bill_cost * .15,
        'bad': bill_cost * .1,
    }
    service_lvl = None
    while service_lvl not in levels:
        service_lvl = input("Was your service good, fair, or bad? ")
        service_lvl = service_lvl.lower()
        if service_lvl in levels:
            print("Your tip amount will be ${:.2f}".format(levels[service_lvl]))
            print("Your bill total will be ${:.2f}".format(levels[service_lvl] + bill_cost))
            break
        else:
            print("Sorry, use only good, fair, or bad as your service level :")

# tip_calc()

# While loop ex 9

# i = -1
# while i < 9:
#     for i in range(1, 11):
#         print(i)

# ex 10

def coin_dispenser():
    new_coin = "yes"
    coin_count = 0
    while new_coin != "no" or new_coin != "n":
        new_coin = input("You have {} coins, would you like a coin? ".format(coin_count))
        new_coin = new_coin.lower()
        if new_coin == "yes" or new_coin == "y":
            coin_count += 1
        elif new_coin == "no" or new_coin == "n":
            print("Bye!")
            break
        else:
            print("Please use only yes or no!")
            
# coin_dispenser()
    