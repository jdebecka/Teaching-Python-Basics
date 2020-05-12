import string


class Person:

    # Called only once when the object is being created
    def __init__(self, name: string, last_name: string, id_number: int):
        self.name = name
        self.partners = list()
        self.last_name = last_name
        self.id_number = id_number

    # Functions can be called as many times as you need them to be called
    def print(self):
        print(self.name, self.last_name)

    def change_name(self, new_name):
        self.name = new_name

    def print_partners(self):
        for partner in self.partners:
            print(partner.name)

    def add_partner(self, person):
        self.partners.append(person)


# Creating objects of a class person
parker = Person("Parker", "Hicks", 124342)
julia = Person("Julia", "Debecka", 32343)

# Calling functions on an object
parker.add_partner(julia)

parker.print_partners()
# parker.change_name("Parker Calvin")
#
# parker.print()
#
# parker.change_name("Parker")
#
# parker.print()


# TODO: Create class shark name, init speed = 0 func faster slow_down + 1
# TODO: speed can't be less than 0

# func __init__(self, uptoyou)
# speed plus/minus
# print
# func addChild(self, Shark)