# Calculate the factorial of a number using lambda function.

from functools import reduce

# Define the factorial lambda function
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage
number = 5
result = factorial(number)
print(result)
