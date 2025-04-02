# ECOR 1042 Lab 4 - Individual submission for test1 function

# import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Kwan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101332749"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

#==========================================#
# Do not modify the code alreayd provided.


def test_return_list() -> list[int]:
    # Complete the function with your test cases
    passes = 0
    fails = 0
    file_name = 'student-test.csv'
    
    test_cases = [
         # test that student_school_list returns a list (3 different test cases required)
        (load_data.student_school_list, [file_name, "MS"]),
        (load_data.student_school_list, [file_name, " "]),
        (load_data.student_school_list, [file_name, "CF"]),
         # test that student_age_list returns a list (3 different test cases required)
        (load_data.student_age_list, [file_name, "17"]),
        (load_data.student_age_list, [file_name, "18"]),
        (load_data.student_age_list, [file_name, "12"]),
        # test that student_health_list returns a list (3 different test cases required)
        (load_data.student_health_list, [file_name, "3"]),
        (load_data.student_health_list, [file_name, "5"]),
        (load_data.student_health_list, [file_name, "0"]),
         # test that student_failures_list returns a list (3 different test cases required)
        (load_data.student_failures_list, [file_name, "3"]),
        (load_data.student_failures_list, [file_name, "1"]),
        (load_data.student_failures_list, [file_name, "8"]),
        # test that load_data returns a list (6 different test cases required)
        (load_data.load_data, [file_name, {'Failures': '0'}]),
        (load_data.load_data, [file_name, {'All': '-1'}]),
        (load_data.load_data, [file_name, {'School': 'BD'}]),
        (load_data.load_data, [file_name, {'FallGrade': '7'}]),
        (load_data.load_data, [file_name, {'WinterGrade': '6'}]),
        (load_data.load_data, [file_name, {'Age': '17'}]),
        # test that add_average returns a list (3 different test cases required)
        (load_data.add_average, [[{'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1, 'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11}]]) ,
        (load_data.add_average, [[{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6}]]) ,
        (load_data.add_average, [[
            {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6},
            {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1, 'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11}
        ]])
    ]
    
    for func, arg in test_cases:
        try:
            assert isinstance(func(*arg), list)
            passes += 1
        except AssertionError:
            print("An error occured: Function " + func.__name__ + " with arguments " + str(arg) + " did not return a list.")
        
            fails += 1
    # return the a list with the number of tests that passed and the number that failed
    return [passes, fails]

if __name__ == "__main__":
    print(test_return_list())
# Do NOT include a main script in your submission
