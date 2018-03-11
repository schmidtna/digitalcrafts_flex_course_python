
# ex 1, 2

import json

grab_file = input("What file would you like to load? ")

user_input = input("Enter data: ")

def load_data():
    with open(grab_file, 'r') as fh:
        return json.load(fh)

def save_data(data):
    with open(grab_file, 'w') as fh:
        return json.dump(user_input, fh)

# data = load_data()

# data['hello'] = 'me'
# data['hello2'] = 'me'

# save_data(user_input)
