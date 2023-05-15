# In this code, the current_case += 1 statement is moved outside of the try-except block and the return statements. This allows the loop to continue iterating until all cases have been processed. Once all cases are processed, the function returns True to indicate that all regex patterns were valid.


import re

num_cases = int(input())
current_case = 1

def reggie(num_cases, current_case):
    while current_case <= num_cases:
        # split as long as there's cases
        next_case = input()
        current_case +=1
        try:
            re.compile(next_case)
            print("True")
        except re.error as e:
            print("False")
reggie(num_cases, current_case)
