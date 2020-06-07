'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
from collections import Counter

string1 = input("Tell me something: ")
list1 = string1.split()
print(list1)

Counter = Counter(list1)
most_occurrences = Counter.most_common()
dict1 = dict(most_occurrences)
maximum = max(dict1, key=dict1.get)
print(maximum, dict1[maximum])