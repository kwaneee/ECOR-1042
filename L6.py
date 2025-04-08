#Unit Testing

#ASSERT Statements
#• An assert statement has the form:
# assert expression, message
# • If expression is True, execution continues quietly (no
# message is displayed)
# • If expression is False, execution halts (by default) and
# an AssertionError is displayed
# • If a message is included, the message is displayed

# Case Study: fibonacci

def fibonacci (n:int) -> int:
    """
    Return the Fibonacci number F_n for positive values
    of n, where F_1 = 1, F_2 = 1, and F_n = F_n-1 + F_n-2,
    n > 2.
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(5)
    5
    """

    a = 1 
    b = 1
    for i in range (1, n): #THERE is a bug here: 2nd argument should be n

        a, b=b, a+b
    return b