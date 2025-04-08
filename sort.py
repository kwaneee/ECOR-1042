# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Elise Katsube, Joshua Kwan, Anjana Ramaswamy, Ailsa Kieser"

# Update "" with your team (e.g. T102)
__team__ = "T017"

# ==========================================#
# Place your sort_students_age_bubble function after this line


# ==========================================#
# Place your sort_students_time_selection function after this line


# ==========================================#
# Place your sort_students_avg_insertion function after this line


# ==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(data: list[dict], order: str) -> str:
    if data == []:
        return "Empty list."
    else:
        failure_check = data[0]
        failures_in_data = False
        for keys in failure_check:
            if keys == "Failures":
                failures_in_data = True
        if failures_in_data == False:
            return "List not sorted. Failures key not present."
        if order == "A":
            swap = True
            while swap:
                swap = False
                for i in range(len(data) - 1):
                    if data[i]['Failures'] > data[i + 1]['Failures']:
                        data[i], data[i + 1] = data[i + 1], data[i]
                        swap = True
            return "List sorted."
        elif order == "D":
            swap = True
            while swap:
                swap = False
                for i in range(len(data) - 1):
                    if data[i]['Failures'] < data[i + 1]['Failures']:
                        data[i], data[i + 1] = data[i + 1], data[i]
                        swap = True
            return "List sorted."

# ==========================================#
# Place your sort function after this line


def sort(student_data: list[dict], order: str, attribute: str) -> str:
    if attribute == "Age":
        sort_students_age_bubble(student_data, order, attribute)
    elif attribute == "StudyTime":
        sort_students_time_selection(student_data, order, attribute)
    elif attribute == "AvgGrade":
        sort_students_avg_insertion(student_data, order, attribute)
    elif attribute == "Failures":
        sort_students_failures_bubble(student_data, order, attribute)
    else:
        return "Invalid input, the list cannot be sorted by " + attribute

# Do NOT include a main script in your submission
