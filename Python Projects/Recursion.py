def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1

    elif x < 0 :
        return False
    else:
        return (x * factorial(x-1))

n = int(input())
print("The factorial of", n, "is", factorial(n))