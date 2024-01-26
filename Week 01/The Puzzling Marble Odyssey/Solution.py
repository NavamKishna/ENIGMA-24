#This program provides a straightforward solution to Alice's marble collection challenge, where the total marbles are calculated by summing up the day numbers between the specified starting and ending days.


def calculate_total_marbles(num1, num2):
    total_marbles = 0
    for day in range(num1, num2 + 1):
        total_marbles += day
    return total_marbles

# Input
num1 = int(input())
num2 = int(input())

# Output
total_marbles_collected = calculate_total_marbles(num1, num2)
print(total_marbles_collected)
