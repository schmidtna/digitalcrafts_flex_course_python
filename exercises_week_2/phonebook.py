

main_menu = ("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")
print(main_menu)

def option_select():
    while True:
        try:
            choice = int(input("Enter your selection number (1-5) "))
            if choice > 0 and choice < 6:
                print(choice)
                break
            else:
                print("Sorry only numbers 1-5 are valid\n")
                print(main_menu)

        except ValueError:
            print("Sorry only numbers are valid (1-5)\n")

            # if choice == 1:
            #     entry_lookup()
            #     break
            # elif choice == 2:
            #     entry_input()
            #     break
            # elif choice == 3:
            #     entry_del()
            #     break
            # elif choice == 4:
            #     lib_list()
            #     break
            # elif choice == 5
            #     break
            
            
option_select()




# contact_list = {
#     "Nick" : "713-504-1010"
    
#     }