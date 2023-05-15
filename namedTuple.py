
# Calculate the student's average marks

# The number of items and student's scores are below:
# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6   


# If the second line of input contains the column names in any order, we need to modify the code to handle the dynamic column order. One way to achieve this is by using a dictionary to map the column names to their corresponding indices.

from collections import namedtuple

num_cases = int(input())
columns = input().split()  # Read the column names

Student = namedtuple('Student', columns) # student namedtuple is defined using the 'columns' list, giving dynamic order capability

students = []

for _ in range(num_cases):
    student_info = input().split()
    student_data = {} # during each iter, 'student_data' dictionary is created, stores student's data
    for column, value in zip(columns, student_info): #zip function pairs each column name with corresponding value in student information
        if column in ['ID', 'MARKS']: #if checkes if current column is 'ID' or 'MARKS'. If yes, value converted to integer w/ int(), else left as 'value'
            student_data[column] = int(value)
        else:
            student_data[column] = value
    student = Student(**student_data) #'student_data' dictionary unpacked using '**' when creating new 'Student' namedtuple
    students.append(student)

total_marks = sum(student.MARKS for student in students)
average = total_marks / len(students)
print('{:.2f}'.format(average))
