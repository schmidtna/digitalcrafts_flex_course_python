
def dict_calls():

    phonebook = {
        "Alice" : "703-009-7345",
        "Bob" : "454-698-1234",
        "Elizabeth" : "456-789-1011"
    }

    print(phonebook["Elizabeth"])
    phonebook["Kareem"] = "893-345-3874"
    del phonebook["Alice"]
    phonebook["Bob"] = "111-111-1111"
    print(phonebook)

# dict_calls()

def nest_dict():

    ramit = {
        "name" : "Ramit",
        "email" : "ramit@gmail.com",
        "interests" : ["movies", "tennis"],
        "friends" : [
            {
                "name" : "Jasmine",
                "email" : "jasmine@gmail.com",
                "interests" : ["photography", "tennis"] 
            },
            {
                "name" : "Jan",
                "email" : "jan@gmail.com",
                "interests" : ["movies", "tv"]
            }
        ]
    }

    # print(ramit["email"])
    # print(ramit["interests"][0])
    # print(ramit["friends"][0]["email"])
    # print(ramit["friends"][1]["interests"][1])
    for i in ramit.keys():
        print(i)

nest_dict()



def letter_count(x):

    input_letters = {}

    for i in x:
        # tries to call key i, if not there returns 0 and generates empty key(i)
        counting = input_letters.get(i, 0)
        # gives empty key(i) a value, and adds +1 to it, or adds +1 to existing value
        input_letters[i] = counting + 1
    
    print(input_letters)

# if __name__ == "__main__":
#     letter_count("hello")

def word_count():

    user_input = input("Let's count : ")
    para_list = user_input.split(" ")
    word_list = {}

    for i in para_list:
        counter = word_list.get(i, 0)
        word_list[i] = counter + 1
        val_list = word_list.values()
       
    print(word_list)
    print(val_list)
    

# if __name__ == "__main__":
#     word_count()




