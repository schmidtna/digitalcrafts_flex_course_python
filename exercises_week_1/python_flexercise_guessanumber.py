import random


def number_game():
    secret_number = random.randint(1, 10)
    chances = 5
    
    print("""I'm thinking of a number between 1 and 10,
        can you guess it? You have {} chances.""".format(chances))
    
    while chances > 0:
        user_input = (input("What is your guess? "))
        if len(user_input) == 0 or user_input.isalpha():
            print("Valid inputs are numbers 1-10 only.")
        elif int(user_input) > 10:
            print("Valid inputs are numbers 1-10 only.")
        elif int(user_input) == secret_number:
            print("You got it! The secret number was {}".format(secret_number))
            break
        elif int(user_input) > secret_number:
            chances -= 1
            print("Your guess was too high! Try again, {} chances left!".format(chances))
        elif int(user_input) < secret_number:
            chances -= 1
            print("Your guess was too low! Try again, {} chances left!".format(chances))
        elif chances == 0:
            break
    

number_game()
        
    

