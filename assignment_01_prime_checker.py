# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================

# Function to check if a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check for divisors
    for i in range(2, number):
        if number % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True


# Main program
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")