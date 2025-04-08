# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ailsa Kieser"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101333812"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

# ==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions

from load_data import *
from curve_fit import *
from sort import *
from histogram import *


user_input = ""
filename = ""
student_data = None
data_loaded = False


while user_input != "E":
    user_input = input(
        "The available commands are:\nL)oad Data\nS)ort Data\nC)urve Fit\nH)istogram\nE)xit\nPlease type your command: ")

    user_input = user_input.upper()

    if user_input == "L":
        filename = input("Please enter the name of the file: ")
        attribute = input("Please enter the attribute to use as a filter: ")

        while attribute != "All" and attribute != "School" and attribute != "Health" and attribute != "Failures" and attribute != "Age":
            print("Invalid attribute.")
            attribute = input(
                "Please enter the attribute to use as a filter: ")

        if attribute == "All":
            student_data = add_average(load_data(filename, {attribute: 0}))
        else:
            value = input("Please enter the value of the attribute: ")
            student_data = add_average(
                load_data(filename, {attribute: value}))
        data_loaded = True
        print("Data loaded.")

    elif data_loaded == True:
        if user_input == "S":
            attribute_2 = input(
                "Please enter the attribute to use as a filter:\n'Age', 'Failures', 'AvgGrade', 'StudyTime': ")
            while attribute_2 != "StudyTime" and attribute_2 != "AvgGrade" and attribute_2 != "Failures" and attribute_2 != "Age":
                print("Invalid attribute.")
                attribute_2 = input(
                    "Please enter the attribute to use as a filter:\n'Age', 'Failures', 'AvgGrade', 'StudyTime': ")

            order = (input("Ascending (A) or Descending (D) order: ")).upper()
            while order != "A" and order != "D":
                print("Invalid command")
                order = (
                    input("Ascending (A) or Descending (D) order: ")).upper()

            display = (input("Do you want to display the data?: ")).upper()
            while display != "Y" and display != "N":
                print("Invalid command")
                display = (
                    input("Do you want to display the data?: ")).upper()

            print(student_data)
            print(order)
            print(attribute_2)
            sort(student_data, order, attribute_2)

            if display == "Y":
                print(student_data)

        elif user_input == "C":
            attribute_3 = input(
                "Please enter the attribute you want to use to find the best fit for AvgGrade: ")
            while attribute_3 != "Age" and attribute_3 != "StudyTime" and attribute_3 != "Failures" and attribute_3 != "Health" and attribute_3 != "Absences" and attribute_3 != "FallGrade" and attribute_3 != "WinterGrade" and attribute_3 != "ID":
                print("Invalid attribute")
                attribute_3 = input(
                    "Please enter the attribute you want to use to find the best fit for AvgGrade: ")

            polynomial = input(
                "Please enter the order of the polynomial to be fitted: ")
            is_integer = False

            while is_integer == False:
                try:
                    int(polynomial)
                except:
                    print("Invalid input. Please enter an integer")
                    polynomial = input(
                        "Please enter the order of the polynomial to be fitted: ")
                else:
                    is_integer = True
            curve_fit(student_data, attribute_3, polynomial)

        elif user_input == "H":
            attribute_4 = input(
                "Please enter the attribute you want to create a histogram for: ")
            while attribute_4 != "Age" and attribute_4 != "StudyTime" and attribute_4 != "Failures" and attribute_4 != "Health" and attribute_4 != "Absences" and attribute_4 != "FallGrade" and attribute_4 != "WinterGrade" and attribute_4 != "ID" and attribute_4 != "AverageGrade":
                print("Invalid attribute")
                attribute_3 = input(
                    "Please enter the attribute you want to create a histogram for: ")
            histogram(student_data, attribute_4)

    elif user_input != "E" and (user_input == "S" or user_input == "C" or user_input == "H"):
        print("File not loaded. Please, load a file first.")

    else:
        print("Invalid command.")


