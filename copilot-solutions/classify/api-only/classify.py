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

NOTE: You must use the function read_from_stdin() defined in lib.py instead of the Python input() function,
      and you must use the function write_to_stdout() defined in lib.py instead of the Python print() function.
      Use from lib import read_from_stdin, write_to_stdout to import the function.
'''

from app.lib import read_from_stdin, write_to_stdout
# Your code goes here
def main():
    input_string = read_from_stdin("input: ")
    if input_string[0] in "aeiouAEIOU":
        write_to_stdout("vowel")
    elif input_string[0] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        write_to_stdout("consonant")
    else:
        write_to_stdout("neither")

main()