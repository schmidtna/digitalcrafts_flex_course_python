import json

main_menu = ("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")

def app_launch():
    global pb
    with open("phonebook.json", "r") as phonebook:
        pb = json.load(phonebook)
       
        option_select()
        
def entry_list(user_library):
    for key in user_library.keys():
        print(user_library[key]["name"])
                      

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
            entry_lookup()
        elif choice == 2:
            entry_input()
        elif choice == 3:
            entry_del()
        elif choice == 4:
            entry_list(pb)
        elif choice == 5:
            run = False
            break





# contact_list = {
#     "Nick" : "713-504-1010"
    
#     }

app_launch()