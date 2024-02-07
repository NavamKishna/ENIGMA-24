# Quadratic Equation Solver

You are tasked with creating a Python function to solve a quadratic equation of the form \( ax^2 + bx + c = 0 \). The function should take three coefficients \( (a, b, c) \) as input and return the roots of the equation. Additionally, it should handle different scenarios based on the discriminant.

## Input Format

The function should take three integers \( a \), \( b \), and \( c \) as parameters.

**Constraints:**
- \( a \neq 0 \)

## Output Format

Output the two roots with a space in between. If the roots are real, return them as floating-point numbers rounded and formatted to two decimals. If the roots are complex, return them as complex numbers, where both real and imaginary parts are rounded and formatted to two decimals. Always print the larger root first then the smaller one.

### Sample Input 0
1 -5 6

### Sample Output 0
3.00 2.00

### Sample Input 1
2 -4 2

### Sample Output 1
1.00 1.00