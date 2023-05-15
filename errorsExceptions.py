# Solution:

num_cases = int(input())
current_case = 1

while current_case <= num_cases:
    # split as long as there's cases
    next_cases = input().split()
    try:
        a = int(next_cases[0])
        b = int(next_cases[1])
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
    current_case +=1











