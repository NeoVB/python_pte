#Write a Python program to create all possible
#strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import itertools

chars = "aeiou"

string = ""

words = [''.join(x) for x in itertools.permutations(chars, 5)]
print (words)
