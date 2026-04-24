#function 1 kevin

#pow(x, y): x raised to the power y


def expo(x,y):
    return f"{x}to the power of {y} is {x**y}"

 
    x = float(input("Base: "))
    y = float(input("Exponent: "))
    expo(x,y)
  
#function 2 kevin

def hypotonuse(a,b):
    return f"The hypotenuse is {(a**2 + b**2)**0.5}"

    a = float(input("Side A is: "))
    b = float(input("Side B is: "))
    hypotonuse(a,b)

#function 1 amadou

#is_prime(x): Check if x is a prime
def is_prime(x):
    """
    Function Name: is_prime

    Purpose:
    This function checks whether a given number is a prime number.

    Parameters:
    x (int): The number to check.

    Return:
    bool: Returns True if x is a prime number, otherwise returns False.
    """

    # Numbers less than 2 are not prime
    if x < 2:
        return False

    # Check divisibility from 2 to x-1
    for i in range(2, x):
        if x % i == 0:
            return False

    # If no divisors found, number is prime
    return True





#function 2 amadou
def sum_of_digits(n):
    """
    Function Name: sum_of_digits

    Purpose:
    This function calculates the sum of all digits in a given number, including negative numbers.

    Parameters:
    n (int): The number whose digits will be summed.

    Return:
    int: The sum of the digits of n.
    """

    total = 0

    # Convert number to string to loop through digits
    for digit in str(abs(n)):
        total += int(digit)

    return total


