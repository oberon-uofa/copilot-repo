'''
Write a program, in a file named median.py, that behaves as follows:

It reads in an input string using the Python statement

input("input: ")

You can assume that the input string will have length at least 1.

It generates output as follows:
if the length of the input string is odd, the middle character of the string is printed;
if the length of the input string is even, the two middle characters of the string are printed.  

Examples:

Input, Output
a, a
ab, ab
567, 6
!@#$%&, #$
'''

def main():
    # Get input
    input_str = input("input: ")
    # Get length of input
    input_len = len(input_str)
    # Get middle index
    middle_index = input_len // 2
    # Get middle character
    middle_char = input_str[middle_index]
    # Print middle character
    print(middle_char)

main()