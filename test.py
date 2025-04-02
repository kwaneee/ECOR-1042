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
    passes=0
    fails=0
    file_name= 'student-test.csv'
    # test that student_school_list returns a list (3 different test cases required)
    final= load_data.student_school_list(file_name, "MS")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1
    final= load_data.student_school_list(file_name, " ")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1 
    final= load_data.student_school_list(file_name, "CF")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1       
    # test that student_age_list returns a list (3 different test cases required)
    final= load_data.student_age_list(file_name, "17")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    final= load_data.student_age_list(file_name, "18")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    final= load_data.student_age_list(file_name, "12")
    if isinstance(final,list):
        passes +=1  
    else:
        fails +=1     
    # test that student_health_list returns a list (3 different test cases required)
    final= load_data.student_health_list(file_name, "3")    
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    final= load_data.student_health_list(file_name, "5")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    final= load_data.student_health_list(file_name, "0")
    if isinstance(final,list):
        passes +=1 
    else:
        fails +=1     
    # test that student_failures_list returns a list (3 different test cases required)
    final= load_data.student_failures_list(file_name, "3")    
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    final= load_data.student_failures_list(file_name, "1")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    final= load_data.student_failures_list(file_name, "8")
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    # test that load_data returns a list (6 different test cases required)
    final= load_data.load_data(file_name, {'Failures' : '0'})
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1 
    final= load_data.load_data(file_name, {'All' : '-1'})
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1 
    final= load_data.load_data(file_name, {'School' : 'BD'})
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1
    final= load_data.load_data(file_name, {'FallGrade' : '7'})
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1
    final= load_data.load_data(file_name, {'WinterGrade' : '6'})
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1
    final= load_data.load_data(file_name, {'Age' : '17'})
    if isinstance(final,list):
        passes +=1
    else:
        fails +=1     
    # test that add_average returns a list (3 different test cases required)
    example_1 = [{'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11}]
    final = load_data.add_average(example_1)
    if isinstance(final, list):
        passes += 1
    else:
        fails += 1
    #
    example_2 = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0,'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6}]
    final = load_data.add_average(example_2)
    if isinstance(final, list):
        passes += 1
    else:
        fails += 1 
    #
    example_3 = [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 7.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 5, 'WinterGrade': 6}, {'School': 'MS', 'ID': 20, 'Age': 20, 'StudyTime': 1.0, 'Failures': 1,'Absences': 10, 'FallGrade': 9, 'WinterGrade': 11}]
    final = load_data.add_average(example_3)
    if isinstance(final, list):
        passes += 1
    else:
        fails += 1    
    # return the a list with the number of tests that passed and the number that failed
    return [passes, fails]

if __name__ == "__main__":
    print(test_return_list())
# Do NOT include a main script in your submission

