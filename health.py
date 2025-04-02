# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Kwan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101332749"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

#==========================================#
# Place your student_health_list function after this line




#def student_health_list(s: str, a: int) -> :

import string

def student_health_list(file_name: str, health_val: int) -> list[dict]:
    """
    Reads a CSV file and returns a list of students (as dictionaries) whose health matches the given value.

    Parameters:
    file_name (str): The name of the CSV file containing student data.
    health_value (int): The health value to filter students.

    Returns:
    list[dict]: A list of dictionaries, each representing a student (excluding the "Health" field).

student_health_list('student-mat.csv', 2)
[ {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,
 'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11},
 {another element},
 …
]
    """

    file = open(file_name, 'r')

    for line in file:

        line = line.strip()
        
        columns = line.split(',')
        


    print(columns)

student_health_list("student-mat.csv", 2)

# Do NOT include a main script in your submission
