'''
Write a script that takes a list and turns it into a tuple.

'''

ask_string = input("Tell me something: ")
list1 = ask_string.split()
tuple1 = tuple(list1)
print(tuple1)