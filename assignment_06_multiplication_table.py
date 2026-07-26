# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================


# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------

def multiplication_table(number):

    if number <= 0:
        print("Error: Number must be a positive integer.")
        return

    print(f"Multiplication Table for {number}:")

    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


# -----------------------------------------------------------------------------
# PART B — Tables from 1 to N
# -----------------------------------------------------------------------------

def multiple_tables(n):

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for number in range(1, n + 1):

        print(f"Multiplication Table for {number}:")

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

        print("---------------------------")


# =============================================================================
# MAIN PROGRAM
# =============================================================================


# Part A
print("PART A — Single Multiplication Table")

num = int(input("Enter a number: "))

multiplication_table(num)


# Part B
print("\nPART B — Multiplication Tables from 1 to N")

n = int(input("Enter N: "))

multiple_tables(n)