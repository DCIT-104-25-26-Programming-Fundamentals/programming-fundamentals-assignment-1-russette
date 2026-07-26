# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

# Function to read a matrix from the user
def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        while True:
            values = input(f"Enter row {i + 1}: ").split()

            if len(values) == cols:
                row = []
                for value in values:
                    row.append(int(value))
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values.")

    return matrix


# Function to display a matrix neatly
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:4}", end="")
        print()


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        transpose.append(new_row)

    return transpose


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------

def multiply_matrices(matrixA, matrixB):
    rows_A = len(matrixA)
    cols_A = len(matrixA[0])

    rows_B = len(matrixB)
    cols_B = len(matrixB[0])

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += matrixA[i][k] * matrixB[k][j]

            row.append(total)

        result.append(row)

    return result


# =============================================================================
# MAIN PROGRAM
# =============================================================================

print("PART A — Matrix Transpose")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


# -----------------------------------------------------------------------------

print("\n\nPART B — Matrix Addition")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix A")
matrixA = read_matrix(rows, cols)

print("\nEnter Matrix B")
matrixB = read_matrix(rows, cols)

print("\nMatrix A + Matrix B:")
display_matrix(add_matrices(matrixA, matrixB))


# -----------------------------------------------------------------------------

print("\n\nPART C — Matrix Multiplication")

rows_A = int(input("Enter number of rows of Matrix A: "))
cols_A = int(input("Enter number of columns of Matrix A: "))

print("\nEnter Matrix A")
matrixA = read_matrix(rows_A, cols_A)


rows_B = int(input("Enter number of rows of Matrix B: "))
cols_B = int(input("Enter number of columns of Matrix B: "))


if cols_A != rows_B:
    print("Matrix multiplication not possible!")
else:
    print("\nEnter Matrix B")
    matrixB = read_matrix(rows_B, cols_B)

    print("\nMatrix A × Matrix B:")
    display_matrix(multiply_matrices(matrixA, matrixB))
