# # Void function <- when the function doesn't return anything
# # Takes no parameters () <- empty brackets
import random
#
# array = [1,2,3,4,5,3]
#
# for item in array:
#     print(item)
import string
import random


# void
def print_my_name():
    a = 2
    a += a
    print(a)
    print("Hello from print_my_name")
    print("Julia")


# print_my_name()


def print_name(name: string):
    print("Hello from print_name")
    name += name
    print(name)


def print_name_default(name="Julia"):
    print("Hello from print_name_default")
    print(name)

print_name_default("Parker")


# # Calling a function


# print_my_name()
# print_name("Julia")
# print()
# print_name_default()
# print_name_default("Bob")

# # TODO: Create a function that will print your favorite food item. It will take no parameters and return nothing
# # TODO: Create a function tat will take your favorite food item and prints it to the console
# # TODO: Remember to call your functions. They are not your high school friends.

# bestNumber = 8
#
# # # variable out of the scope
# # # you create new bestNumber here and initialize it with 10
#
# def favorite_number():
#     bestNumber2 = 10
#     print(bestNumber2)
#
#
# favorite_number()
#
# print(bestNumber)
#
#
# def favorite_number_pass_value(number):
#     print(number)
#
#
# favorite_number_pass_value(bestNumber)
# print(bestNumber)
#
#
def change_best_number(number):
    return number + 2


def get_random():
    return random.random()


print(ty)
#
#
# print("Before change_best_number: ", bestNumber)
# bestNumber = change_best_number(bestNumber)
# print("After change_best_number: ", bestNumber)

# # TODO: Create function add that will take two numbers adds them together and returns the result

# # TODO: Big challenge: Create simple program that will act like calculator.


# # Create 2 functions add and subtract and one helper function that will take 2 numbers and an operator and decides
# if it should call add function or subtract based on the passed operator
# then return the result and print output to the console
# HINT: <- I will provide if wanted
