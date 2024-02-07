# In this task, our goal is to calculate the sum of Fibonacci numbers within a given range of positions efficiently. 
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers. 
# Given two integers `a` and `b` representing the range of positions in the sequence (1 <= a <= b <= 1000), 
# the function must compute the sum of Fibonacci numbers from the ath to the bth position inclusively. 
# To achieve this, an efficient approach involves iterating through the Fibonacci sequence while keeping track of the sum within the specified range, 
# ensuring the solution can handle larger values of `a` and `b` effectively.


def fibonacci_sum(a, b):
    # Initialize Fibonacci sequence with the first two numbers
    fib_sequence = [0, 1]

    # Extend the sequence up to the bth position
    while len(fib_sequence) <= b:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Calculate the sum from ath to bth position
    fib_sum = sum(fib_sequence[a-1:b])

    return fib_sum

# Example usage
a = int(input())
b = int(input())

result = fibonacci_sum(a, b)
print(result)
