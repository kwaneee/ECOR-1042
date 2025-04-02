# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Ailsa Kieser, Anjana Ramaswamy, Elise Katsube, Joshua Kwan"

# Update "" with your team (e.g. T102)
__team__ = "T-017"

# ==========================================#
# Place your student_school_list function after this line


def student_school_list(filename: str, school_name: str) -> list:
    """Returns the list of students as dictionaries that attended the school.
    >>> student_school_list('student-mat.csv', 'GP')
    [ {'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3,
    'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6 },
    {another element},
    ...
    ]
    >>> student_school_list('student-mat.csv', 'SYSC2006')
    []
    >>> student_school_list('student-mat.csv', 'BD')
    [ {'ID': 240, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 2, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 7},
    {another element},
    ...
    ]
    """
    file = open(filename, 'r')
    students = []
    Once = False

    for line in file:
        student_data = line.strip().split(',')
        if Once == False:
            Once = True
            header = line.strip().split(',')
            del header[0]
        if student_data[0] == school_name:
            student_data = student_data[1:]
            student_data = [int(student_data[0]), int(student_data[1]), float(student_data[2]), int(
                student_data[3]), int(student_data[4]), int(student_data[5]), int(student_data[6]), int(student_data[7])]
            students.append(dict(zip(header, student_data)))

    file.close()
    return students

# ==========================================#
# Place your student_health_list function after this line


def student_health_list(file_name: str, health_val: int) -> list:
    """
    ReturnReads a list of students (as dictionaries) whose health matches the given value, after reading a CSV file


>>> student_health_list('student-mat.csv', 2)
[ {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,
 'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11},
 {another element},
 …
]
    """

    file = open(file_name, 'r')
    list = []
    head = True

    for line in file:
        columns = line.strip().split(',')

        if head == True:
            header = [columns[0], columns[1], columns[2], columns[3],
                      columns[4], columns[6], columns[7], columns[8]]
            head = False
        elif head == False and columns[5] == str(health_val):
            columns[1] = int(columns[1])
            columns[2] = int(columns[2])
            columns[3] = float(columns[3])
            columns[4] = int(columns[4])
            del (columns[5])
            columns[5] = int(columns[5])
            columns[6] = int(columns[6])
            columns[7] = int(columns[7])

            columns_in_dict = zip(header, columns)
            list.append(dict(columns_in_dict))

    file.close()
    return list

# ==========================================#
# Place your student_age_list function after this line


def student_age_list(filename: str, age: int) -> list[dict]:
    """Return a list of dictionaries about a set of students with the same age as the 'age' input parameter. The dictionaries contain every key except the age of the student.
    >>> student_age_list('student-mat.csv', 15)
    [{'School': 'GP', 'ID': 201, 'StudyTime': 4.0, 'Failures': 3, 'Health': 3,'Absences': 6, 'FallGrade': 7, 'WinterGrade': 8}, {another element},...]
    >>> student_age_list('student-mat.csv', 0)
    []
    >>> student_age_list('student-mat.csv', 18)
    [{'School': 'GP', 'ID': 1, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5}, 'WinterGrade': 6}, {another element},...]
    """
    file = open(filename, "r")
    first_row = True
    age_list = []

    for line in file:
        student_list = line.strip().split(',')
        if first_row == True:
            keys_age = [student_list[0], student_list[1], student_list[3],
                        student_list[4], student_list[5], student_list[6], student_list[7], student_list[8]]
            first_row = False
        elif first_row == False and student_list[2] == str(age):
            student_list[1] = int(student_list[1])
            del (student_list[2])
            student_list[2] = float(student_list[2])
            student_list[3] = int(student_list[3])
            student_list[4] = int(student_list[4])
            student_list[5] = int(student_list[5])
            student_list[6] = int(student_list[6])
            student_list[7] = int(student_list[7])
            final = zip(keys_age, student_list)
            age_list.append(dict(final))

    file.close()
    return age_list

# ==========================================#
# Place your student_failures_list function after this line


def student_failures_list(file_name: str, fail_num: int) -> list[dict]:
    """Return a list containing the information of the students (as a dictionary
    sans number of failures) whose number of fails are the same as the fail_num
    input parameter.

    Preconditions: N/A

    >>>student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade' : 6}, ...]
    >>>student_failures_list('student-mat.csv', 40)
    []
    >>>student_failures_list('student-mat.csv', 2)
    [{'School': 'GP', 'ID': 26, 'Age': 16, 'StudyTime': 1.5, 'Health': 5, 'Absences': 14, 'FallGrade': 6, 'WinterGrade' : 9}, ...]
    """
    open_file = open(file_name, "r")
    fail_list = []
    row_1 = True

    for line in open_file:
        student_data = line.strip().split(',')
        if row_1 == True:
            keys_fails = [student_data[0], student_data[1], student_data[2], student_data[3],
                          student_data[5], student_data[6], student_data[7], student_data[8]]
            row_1 = False
        elif row_1 == False and student_data[4] == str(fail_num):
            del (student_data[4])
            student_data[1] = int(student_data[1])
            student_data[2] = int(student_data[2])
            student_data[3] = float(student_data[3])
            student_data[4] = int(student_data[4])
            student_data[5] = int(student_data[5])
            student_data[6] = int(student_data[6])
            student_data[7] = int(student_data[7])
            student_dict = zip(keys_fails, student_data)
            fail_list.append(dict(student_dict))

    open_file.close()
    return fail_list

# ==========================================#
# Place your load_data function after this line


def load_data(file_name: str, student_dict: dict) -> list[dict]:
    """Return a list containing the information of the students (as a dictionary)
    whose information matches the given attribute. Inputting "All" as the key of
    the input dictionary will return the information of all of the students, and
    inputting a key that does not exist returns an empty list with an error message.

    Preconditions: N/A

    >>>load_data('student-mat.csv', {'Failures': 0})
    [{'School': 'GP', 'ID': 22, 'Age': 18, 'StudyTime':7.0, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}, {another element}, …]
    >>>load_data('student-mat.csv', {'All': -1})
    [{'School': 'GP', 'ID': 22, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 13}, {another element}, …]
    >>>load_data('student-mat.csv', {'G1': 10})
    Invalid Value
    []
    """
    function_name = []
    input_value = []
    items = student_dict.items()

    for item in items:
        function_name.append(item[0]), input_value.append(item[1])

    if function_name[0] == "School":
        return student_school_list(file_name, input_value[0])
    elif function_name[0] == "Age":
        return student_age_list(file_name, input_value[0])
    elif function_name[0] == "Health":
        return student_health_list(file_name, input_value[0])
    elif function_name[0] == "Failures":
        return student_failures_list(file_name, input_value[0])
    elif function_name[0] == "All":
        open_file = open(file_name, "r")
        return_list = []
        row_1 = True

        for line in open_file:
            all_student_data = line.strip().split(',')
            if row_1 == True:
                keys = [all_student_data[0], all_student_data[1], all_student_data[2], all_student_data[3],
                        all_student_data[4], all_student_data[5], all_student_data[6], all_student_data[7], all_student_data[8]]
                row_1 = False
            else:
                all_student_data[1] = int(all_student_data[1])
                all_student_data[2] = int(all_student_data[2])
                all_student_data[3] = float(all_student_data[3])
                all_student_data[4] = int(all_student_data[4])
                all_student_data[5] = int(all_student_data[5])
                all_student_data[6] = int(all_student_data[6])
                all_student_data[7] = int(all_student_data[7])
                all_student_data[8] = int(all_student_data[8])
                all_student_dict = zip(keys, all_student_data)
                return_list.append(dict(all_student_dict))

        open_file.close()
        return return_list
    else:
        print("Invalid Value")
        return []

# ==========================================#
# Place your add_average function after this line
def add_average(lst: list) -> list:
    """
    Return the average of the students fall and winter grade as an additional attribute to the dictionary(ies) given.
    >>> add_average([ {'School': 'BD', 'ID': 265, 'Age': 18, 'StudyTime': 3,
    'Failures': 0, 'Health': 3, 'Absences': 0,
    'FallGrade':9, 'WinterGrade': 10},
    {another element},
    … ] )
    [ {'School': 'BD', 'ID': 265, 'Age': 18, 'StudyTime': 3,
    'Failures': 0, 'Health': 3, 'Absences': 0,
    'FallGrade': 9, 'WinterGrade': 10, 'AvgGrade':9.5},
    {another element},
    … ]
    >>> add_average([ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'FallGrade': 5, 'WinterGrade': 6},
    {another element},
    … ] )
    [ {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0,
    'Failures': 1, 'Health': 3, 'Absences': 7,
    'FallGrade': 5, 'WinterGrade': 6, 'AvgGrade':5.50},
    {another element},
    … ]
    >>> add_average([ {'School': 'MS', 'ID': 395, 'Age': 19, 'StudyTime': 1,
    'Failures': 0, 'Health': 5, 'Absences': 5,
    'FallGrade': 8, 'WinterGrade': 9},
    {another element},
    … ] )
    [ {'School': 'MS', 'ID': 395, 'Age': 19, 'StudyTime': 1,
    'Failures': 0, 'Health': 5, 'Absences': 5,
    'FallGrade': 8, 'WinterGrade': 9, 'AvgGrade': 8.5},
    {another element},
    … ]
    """

    for student in lst:
        if 'FallGrade' in student and 'WinterGrade' in student:
            student['FallGrade'] = int(
                student['FallGrade'])
            student['WinterGrade'] = int(
                student['WinterGrade'])
            student['AvgGrade'] = (
                student['FallGrade'] + student['WinterGrade']) / 2
    return lst


# Do NOT include a main script in your submission