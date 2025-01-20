#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a given non-negative integer.

    The factorial of a number n is defined as:
        n! = n * (n-1) * (n-2) * ... * 1 for n > 0
        0! = 1 by definition

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number.

    Raises:
    RecursionError: If the input causes a recursion depth limit to be exceeded.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial(n-1)
        return n * factorial(n-1)


if __name__ == "__main__":
    """
    Main entry point of the script.

    The script takes a single command-line argument (a non-negative integer),
    calculates its factorial using the `factorial` function, and prints the result.

    Usage:
        ./factorial.py <number>

    Example:
        ./factorial.py 4
        Output:


