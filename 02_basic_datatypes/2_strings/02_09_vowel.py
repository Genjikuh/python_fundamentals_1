'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
quote = input("Please tell me something")
print("# a:",quote.count("a"))
print("# e:",quote.count("e"))
print("# i:",quote.count("i"))
print("# o:",quote.count("o"))
print("# u:",quote.count("u"))