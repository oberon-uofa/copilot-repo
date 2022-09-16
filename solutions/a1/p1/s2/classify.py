'''
Write a program, in a file named classify.py, that behaves as follows:

It reads in an input string using the Python statement
input("input: ")
You can assume that the input string will have length at least 1.

It generates output as follows:
if the first character of the input string is a vowel (upper or lower case), the output is: vowel
if the first character is a consonant (upper or lower case), the output is: consonant
if the first character is neither a vowel nor a consonant, the output is: neither

Examples:
Input, Output
apple, vowel
CSc 120, consonant
32F = 0C, neither
'Twas brillig, neither
'''

# Your code goes here

def main():
    input_string = input("input: ")
    if input_string[0] in "aeiouAEIOU":
        print("vowel")
    elif input_string[0] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        print("consonant")
    else:
        print("neither")