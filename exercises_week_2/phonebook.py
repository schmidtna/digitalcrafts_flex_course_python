import json

main_menu = ("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. Contact list
5. Quit
""")

def app_launch():
    global pb
    with open("phonebook.json", "r") as phonebook:
        pb = json.load(phonebook)
       
        option_select()

def entry_lookup(user_library):
    name_in = input("Which contact would you like to view? ")
    name_in = name_in.lower()
    if name_in in user_library:
        print(user_library[name_in]["name"])
        print(user_library[name_in]["number"])
    else:
        print("Contact not found, check contact list and enter name as shown.")
        
def entry_input(user_library):
    name_in = input("Enter your contacts name : ")
    phone_in = input("Enter your contacts phone number :")
    name_in = name_in.lower()
    phone_in = phone_in.lower()
    user_library[name_in] = {"name" : name_in, "number" : phone_in}
    print("Contact {} added with phone number {}".format(name_in, phone_in))

def entry_del(user_library):
    name_del = input("Which entry would you like to remove?")
    if name_del in user_library:
        del user_library[name_del]
        print("Entry for {} removed.".format(name_del))
    else:
        print("Contact not found, check contact list and enter name as shown.")

def entry_list(user_library):
    for key in user_library.keys():
        print(user_library[key]["name"])

def save_changes():
    with open("phonebook.json", "w") as phonebook:
        json.dump(pb, phonebook)

                      

def option_select():
    
    run = True
    while run:
        print(main_menu)
        try:
            choice = int(input("Enter your selection number (1-5) "))
        except ValueError:
            print("Sorry only numbers 1-5 are valid.\n")

        if choice < 1 or choice > 5:
            print("Sorry only numbers 1-5 are valid.\n")
        elif choice == 1:
            entry_lookup(pb)
        elif choice == 2:
            entry_input(pb)
        elif choice == 3:
            entry_del(pb)
        elif choice == 4:
            entry_list(pb)
        elif choice == 5:
            save_changes()
            run = False
            break





# contact_list = {
#     "Nick" : "713-504-1010"
    
#     }

app_launch()