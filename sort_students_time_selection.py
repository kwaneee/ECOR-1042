# ECOR 1042 Lab 5 - Individual submission for sort_students_time_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Kwan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101332749"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-017"

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(a:list, sort:str) -> str:
    """
    Return a sorted string if "Study time" is a key in dictionary. If string is empty, return "Empty List." and if "Study time" is not a key in dictionary, return "List not sorted. StudyTime key not present."
    
    >>> a = []
    >>> sort_students_time_selection (a, "D")
    <a is not modified>
    Empty list.
    >>> a = [{"StudyTime":10,"School":"GP"}, {"StudyTime":19,"School":"MS"}]
    >>> sort_students_time_selection (a, "D")
    <a is now sorted: a = [{"StudyTime": 19, "School":"MS"}, {"StudyTime":10,
    "School":"GP"}] >
    List sorted.
    >>> a = [{"School":"GP"}, {"School":"MS"}]
    >>> sort_students_time_selection (a, "D")
    <a is not modified>
    List not sorted. StudyTime key not present.

    """
    if not a:
        return "Empty list."
    for b in a:
            if "StudyTime" not in b:
                return "List not sorted. StudyTime key not present."
    n=len(a)
    for i in range(n):
        max_i = i        
        for j in range(i+1,n):
            if sort == "A":
                if a[max_i]["StudyTime"] > a[j]["StudyTime"]:
                    max_i = j
            elif sort == "D":
                if a[max_i]["StudyTime"] < a[j]["StudyTime"]:
                    max_i = j             
        a[i],a[max_i] = a[max_i], a[i]
    return "List sorted."
# Do NOT include a main script in your submission
