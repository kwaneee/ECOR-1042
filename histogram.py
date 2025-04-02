# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Kwan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101332749"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt


def histogram(data_set, att):
    """
    Return a histogram and return -1 if the attribute is categorical (School) and the maximum value for the given attribute if it is numerical

    >>> data = [{'School': 'A', 'Score': '90'}, {'School': 'B', 'Score': '80'}, {'School': 'A', 'Score': '85'}]
    >>> histogram(data, 'Score')
    90.0

    >>> data = [{'School': 'A', 'Score': '90'}, {'School': 'B', 'Score': '80'}, {'School': 'A', 'Score': '85'}]
    >>> histogram(data, 'School')
    -1

    >>> data = [{'School': 'A', 'Score': '70'}, {'School': 'B', 'Score': '60'}, {'School': 'A', 'Score': '75'}]
    >>> histogram(data, 'Score')
    75.0

    """

    values = []

    for record in data_set:
        values.append(record[att])

    try:
        float(values[0])
        number_value = []

        for val in values:
            number_value.append(float(val))
            max_value = number_value[0]

        for val in number_value:
            if val > max_value:
                max_value = val
        interval = max_value / 10
        box = [0] * 10

        for val in number_value:
            if val == max_value:
                box_index = 9
            else:
                box_index = int(val // interval)
            box[box_index] += 1
        a = []

        for i in range(10):
            a.append(str(i * interval))
        b = box
        fig = plt.figure()
        plt.title(f"{att} Distribution")
        plt.xlabel(att)
        plt.ylabel('Number of occurences')
        plt.bar(a, b, color='gold')
        plt.show()
        return max_value
    
    except ValueError:
        value_in_dict = {}

        for i in values:
            num = value_in_dict.get(i, 0)
            value_in_dict[i] = num + 1
        a = sorted(value_in_dict)
        b = []

        for i in a:
            b.append(value_in_dict[i])
        fig = plt.figure()
        plt.title(f"{att} Distribution")
        plt.xlabel(att)
        plt.ylabel('Number of occurences')
        plt.bar(a, b, color='gold')
        plt.show()

        return -1
# Do NOT include a main script in your submission
