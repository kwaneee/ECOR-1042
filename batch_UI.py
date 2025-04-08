# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Anjana Ramaswamy"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101336058"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

# ==========================================#
# Place your script for your batch_UI after this line
# You are allowed to create auxiliary functions

from load_data import *
from curve_fit import *
from sort import *
from histogram import *

student_data = None
data_loaded = False

command_filename = input(
    "Please enter the name of the file where your commands are stored: ")
command_file = open(command_filename, "r")
i = 0

for line in command_file:
    command_data = line.strip().split(';')
    command_data[i] = command_data[i].upper()
    if command_data[i] == "L":
        data_filename = command_data[i + 1]
        attribute = command_data[i + 2]
        if attribute == "All":
            student_data = add_average(
                load_data(data_filename, {attribute: 0}))
        else:
            attribute_value = command_data[i + 3]
            student_data = add_average(
                load_data(data_filename, {attribute: attribute_value}))
        data_loaded = True
        print("Data loaded.")
    elif data_loaded == True:
        if command_data[i] == "S":
            sort_attribute = command_data[i + 1]
            order = command_data[i + 2].upper()
            display = command_data[i + 3].upper()
            sort(student_data, order, sort_attribute)
            print("List sorted.")
            if display == "Y":
                print(student_data)
        elif command_data[i] == "C":
            curve_attribute = command_data[i + 1]
            polynomial = int(command_data[i + 2])
            curve_fit(student_data, curve_attribute, polynomial)
        elif command_data[i] == "H":
            histogram_attribute = command_data[i + 1]
            histogram(student_data, histogram_attribute)
    elif command_data[i] != "E" and (command_data[i] == "S" or command_data[i] == "C" or command_data[i] == "H"):
        print("File not loaded. Please, load a file first.")
    else:
        command_file.close()
