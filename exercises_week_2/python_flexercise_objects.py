class Person:
    def __init__(self, name, email, phone, friends, greet_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greet_count = 0

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greet_count += 1

    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number : {} and has greeted {} times.".format(
            self.name, self.phone,self.name, self.email, self.greet_count))

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def __str__(self):
        return "Person : {}, {}, {}".format(self.name, self.email, self.phone)

sonny = Person("Sonny", "sonny@gmail.com", "111-111-1111", [], 0)
jordan = Person("Jordan", "jordan@gmail.com", "222-222-2222", [], 0)

# sonny.greet(jordan)
# jordan.greet(sonny)
# sonny.print_contact_info()
# jordan.print_contact_info()
# sonny.add_friend(jordan)
# print(len(sonny.friends))
# sonny.greet(jordan)
# sonny.print_contact_info()

print(jordan)


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle("Nissan", "Leaf", 2015)

# car.print_info()

