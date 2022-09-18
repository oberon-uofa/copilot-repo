'''
In a file triangle2.py write a recursive function triangle2(n) that returns a triangular array L of size n whose elements are defined as follows:
len(L[k]) = k+1  for 0 < k < N (definition of triangular arrays); 
L[0] = [1];
suppose that the last element of L[i] is the integer m, then the first element of L[i+1] is m+1.
Some examples are given below.
1.1.2. Programming requirements
Your code must satisfy the following requirements:
The code to construct the triangular array must limit itself to the following Python constructs:
if statements
return statements
function calls (including recursive calls)
arithmetic and comparison operations
Python list operations, e.g., indexing, slicing, append, concatenation/extension, + and *
Helper functions are allowed for this problem.

Examples
triangle(2), [[1], [2, 3]]
triangle(3), [[1], [2,3], [4,5,6]]
triangle(4), [[1], [2,3], [4,5,6], [7,8,9,10]]
triangle(5), [[1], [2,3], [4,5,6], [7,8,9,10], [11,12,13,14,15]]
'''

def triangle2(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    else:
        L = triangle2(n-1)
        L.append([L[-1][-1] + 1 + i for i in range(n)])
        return L