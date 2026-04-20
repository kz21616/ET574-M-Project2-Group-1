#function 1 kevin

#pow(x, y): x raised to the power y




#function 2 kevin






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


