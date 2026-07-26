# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================

# Function to calculate sum of numbers
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# Function to calculate average of numbers
def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


# Function to find maximum value
def calculate_maximum(numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


# Function to find minimum value
def calculate_minimum(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum


# Main program

N = int(input("How many numbers? "))

# Check if N is positive
if N <= 0:
    print("Error: Number of values must be positive.")
else:
    numbers = []

    # Read numbers from user
    for i in range(N):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    # Display results
    print("\nResults:")
    print("Sum:    ", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", calculate_maximum(numbers))
    print("Minimum:", calculate_minimum(numbers))