# Using the formula for the nth triangular number to calculate the position
# The formula for the nth triangular number is T_n = n * (n + 1) / 2
# It expresses the sum of natural numbers up to the nth term, forming an equilateral triangle with points.
# Here, 'n' represents the position in the sequence.


# Taking user input as an integer representing a triangular number
n = int(input())

position = int((2 * n + 0.25) ** 0.5 - 0.5)

# Printing the calculated position
print(position)
