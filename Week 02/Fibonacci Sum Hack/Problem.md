# Unraveling the Secret of Fibonacci Numbers

You are summoned to unravel the secret of Fibonacci numbers, the cryptic sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89... Each number, a piece of a mathematical puzzle, is revealed by the arcane formula: \( F_n = F_{n-1} + F_{n-2} \), where the saga begins with \( F_0 = 0 \) and \( F_1 = 1 \).

Your mission, should you choose to accept it, is to craft a function that calculates the sum of Fibonacci numbers from the \( a^{th} \) to the \( b^{th} \) position.

## Input Format
Two integers, \( a \) and \( b \) (\( 1 \leq a \leq b \leq 1000 \)), representing the range of positions in the Fibonacci sequence.

**Constraints:**
\( 1 \leq a \leq b \leq 1000 \)

## Output Format
An integer representing the sum of Fibonacci numbers from the \( a^{th} \) to the \( b^{th} \) position.

### Example:
Fibonacci sum(3, 7)
19

**Explanation:**
The sum of Fibonacci numbers from the 3rd to the 7th position (1 + 2 + 3 + 5 + 8 ) equals 19.

### Sample Input 0
`5`
`10`

### Sample Output 0
`84`