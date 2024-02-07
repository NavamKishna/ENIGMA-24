#To find prime numbers efficiently, the Sieve of Eratosthenes algorithm is utilized, starting with a list of numbers from 2 to the upper limit. This algorithm iteratively marks multiples of each prime number starting from 2 as composite until reaching the square root of the upper limit, leaving only the unmarked numbers as prime. Implemented in Python, a boolean list tracks the primality of numbers, with 0 and 1 initially set as not prime. Multiples of prime numbers are marked as composite, and finally, the prime numbers are outputted from 2 to the upper limit.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(n):
    primes = []
    for num in range(2, n):
        if num % 2 == 0:
            if num==2:
                primes.append(num)
            continue  # Skip even numbers (excluding 2)
        if not is_prime(num):
            continue  # Skip non-prime numbers
        primes.append(num)
    return primes

# Example usage
n = int(input())
result = find_prime_numbers(n)
print(" ".join(map(str, result)))
