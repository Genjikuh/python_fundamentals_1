'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
'''

quote1 = input("Tell me something")
quote2 = input("Tell me more")
quote3 = input("One last thing please")
print(len(quote1), quote1)
print(len(quote2), quote2)
print(len(quote3), quote3)
'''
import operator

quote1 = input("Tell me something")
quote2 = input("Tell me more")
quote3 = input("One last thing please")

longest = 0

dict1 = {quote1 :len(quote1), quote2 : len(quote2), quote3 : len(quote3)}

biggest = max(dict1.items(), key = operator.itemgetter(1))[0]
print(biggest)

