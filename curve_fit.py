# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Elise Katsube"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333124"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

# ==========================================#
# Place your curve_fit function after this line
import numpy as np
import matplotlib.pyplot as plt


def curve_fit(lst: list, attribute: str, degree: int) -> str:
    """Returns a string representation of the equation of best fit for the average grade
    >>> curve_fit([{"AvgGrade":7.2,"Age":"18"}, {"AvgGrade":9.0,"Age":"16"}, {"AvgGrade":7.2,"Age":"17"}, {"AvgGrade":9.1,"Age":"16"},{"AvgGrade":2.3,"Age":"18"}], "Age", 2)
    'y = -0.3x^2+8.05x-42.95'
    >>> curve_fit([{"AvgGrade":7.2,"StudyTime":"2.0"}, {"AvgGrade":9.0,"StudyTime":"4.3"}, {"AvgGrade":7.2,"StudyTime":"3.2"}, {"AvgGrade":9.1,"StudyTime":"4.5"}], "StudyTime", 2)
    'y = 0.59x^2-3.01x+10.84'
    >>> curve_fit([{"AvgGrade":7.2,"Failures":"0"}, {"AvgGrade":9.0,"Failures":"3"}, {"AvgGrade":8.2,"Failures":"2"}, {"AvgGrade":5.6,"Failures":"4"}, {"AvgGrade":9.1,"Failures":"1"}], "Failures", 3)
    'y = -0.12x^3+0.06x^2+1.21x+7.35'
    """
    y_values = []
    x_values = []
    for dictionary in lst:
        value = float(dictionary[attribute])
        x_values += [value]

    for dictionary in lst:
        y = dictionary["AvgGrade"]
        y_values += [y]
    attribute_dict = {}
    attribute_dict = {}
    for x, y in zip(x_values, y_values):
        if x not in attribute_dict:
            attribute_dict[x] = []
        attribute_dict[x].append(y)

    x_unique = sorted(attribute_dict.keys())
    y_avg = [sum(attribute_dict[x]) / len(attribute_dict[x])
             for x in x_unique]

    degree = min(degree, len(x_unique) - 1)

    coefficients = np.polyfit(x_unique, y_avg, degree)

    equation = "y = "

    power = degree

    for i in range(len(coefficients)):
        coeff = coefficients[i]

        if coeff > 0 and i != 0:
            equation += '+'
        elif coeff < 0:
            equation += '-'
            coeff = abs(coeff)

        coeff_str = str(round(coeff, 2))

        if power > 1:
            equation += coeff_str + 'x^' + str(power)
        elif power == 1:
            equation += coeff_str + 'x'
        else:
            equation += coeff_str
        power -= 1

    return equation

    # return str(poly_equation)


# Do NOT include a main script in your submission
