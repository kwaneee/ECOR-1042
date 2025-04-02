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


def student_health_list(file_name: str, health_val: int) -> list:
    """
    Return a list of students (as dictionaries) whose health matches the given value, after reading a CSV file


>>> student_health_list('student-mat.csv', 2)
[ {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,
 'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11},
 {another element},
 …
]
>>> student_health_list('student-mat.csv', 3)
[ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0,
 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
 {another element},
 …
]
>>> student_health_list('student-mat.csv', a)
[]
    """

    file = open(file_name, 'r')
    list = []
    head = True

    for line in file:
        columns = line.strip().split(',')

        # if head == False:
        #     head = True
        #     #header = line.strip().split(',')
        #     head = columns
        #     #del header[5]

        if head == True:
            #header = line.strip().split(',')
            header = [columns[0], columns[1], columns[2], columns[3], columns[4], columns[6], columns[7], columns[8]]
            head = False

        #elif int(columns[5]) == health_val:
        elif head == False and columns[5] == str(health_val):
        
            # print(columns)
            # columns = [int(columns[0]), int(columns[1]), int(columns[2]),float(columns[3]), int(columns[4]), int(columns[5]), int(columns[6]), int(columns[7])]
            #columns[0] = str(columns[0])
            columns[1] = int(columns[1])
            columns[2] = int(columns[2])
            columns[3] = float(columns[3])
            columns[4] = int(columns[4])
            del (columns [5])
            columns[5] = int(columns[5])
            columns[6] = int(columns[6])
            columns[7] = int(columns[7])
            #columns[8] = int(columns[8])

            columns_in_dict = zip(header, columns)
            list.append(dict(columns_in_dict))

    file.close()
    return list

student_health_list("student-mat.csv", 2)

# Do NOT include a main script in your submission
