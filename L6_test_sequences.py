from L6 import fibonacci
def test_fibonacci () -> int:

    # VERSION 1:
    # tests = 0
    # assert fibonacci(1) == 1, 'Wrong value for fibonacci(1)'
    # tests += 1
    # assert fibonacci(2) == 1, 'Wrong value for fibonacci(2)'
    # tests += 1
    # assert fibonacci(3) == 2, 'Wrong value for fibonacci(3)'
    # tests += 1
    # assert fibonacci(5) == 5, 'Wrong value for fibonacci(5)'
    # tests += 1
    # return tests


    #VERSION 2:
    # test_values = [1,2,3,5]
    # expected_outputs = [1,1,2,5]
    # tests = 0

    # for i in range (len(test_values)):
    #     assert fibonacci(test_values[i]) == expected_outputs [i], 'Incorrect value for fibonacci( ' + str(test_values[i])+ ')'
    #     tests += 1
    # return tests

    test_values = [1,2,3,5]
    expected_outputs = [1,1,2,5]
    tests_pass = 0
    tests_fail = 0

    for i in range (len(test_values)):
        try:
            assert fibonacci(test_values[i]) == expected_outputs [i], 'Incorrect value for fibonacci( ' + str(test_values[i])+ ')'
            tests_pass += 1
        except AssertionError as msg:
            print(msg)
            tests_fail += 1
    return (tests_pass, tests_fail)

if __name__ == '__main__':
    passed, failed = test_fibonacci()
    print(passed, 'tests passsed, ', failed, 'tests failed')

