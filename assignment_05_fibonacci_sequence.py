# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================


# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------

def fibonacci_sequence(n):
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    a = 0
    b = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(a, end=" ")

        # Calculate next Fibonacci number
        next_number = a + b
        a = b
        b = next_number

    print()


# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------

def is_fibonacci(number):

    if number < 0:
        print(f"{number} is NOT a Fibonacci number.")
        return

    a = 0
    b = 1

    while a <= number:

        if a == number:
            print(f"{number} is a Fibonacci number.")
            return

        next_number = a + b
        a = b
        b = next_number

    print(f"{number} is NOT a Fibonacci number.")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

# Part A
print("PART A — Fibonacci Sequence Generator")

terms = int(input("How many terms? "))

fibonacci_sequence(terms)


# Part B
print("\nPART B — Fibonacci Number Checker")

number = int(input("Enter a number to check: "))

is_fibonacci(number)