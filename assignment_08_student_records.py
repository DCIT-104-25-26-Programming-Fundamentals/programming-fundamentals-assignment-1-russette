# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================


# -----------------------------------------------------------------------------
# Function to add a student
# -----------------------------------------------------------------------------

def add_student(students):

    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    number_of_scores = int(input("How many scores? "))

    scores = []

    for i in range(number_of_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)

    print(f'Student "{name}" added successfully.')


# -----------------------------------------------------------------------------
# Function to display all students
# -----------------------------------------------------------------------------

def display_students(students):

    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("-" * 60)
    print(f"{'Name':15} {'ID':12} {'Scores':20} {'Average'}")
    print("-" * 60)

    for student in students:

        total = 0

        for score in student["scores"]:
            total += score

        average = total / len(student["scores"])

        scores_string = ", ".join(map(str, student["scores"]))

        print(f"{student['name']:15} {student['id']:12} {scores_string:20} {average:.2f}")

    print("-" * 60)


# -----------------------------------------------------------------------------
# Function to calculate average score for a specific student
# -----------------------------------------------------------------------------

def calculate_average(students):

    student_id = int(input("Enter student ID: "))

    for student in students:

        if student["id"] == student_id:

            total = 0

            for score in student["scores"]:
                total += score

            average = total / len(student["scores"])

            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Student ID not found.")


# -----------------------------------------------------------------------------
# Function to display menu
# -----------------------------------------------------------------------------

def display_menu():

    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


# =============================================================================
# MAIN PROGRAM
# =============================================================================

students = []


while True:

    display_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":

        add_student(students)

    elif choice == "2":

        display_students(students)

    elif choice == "3":

        calculate_average(students)

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid choice. Please enter a number between 1 and 4.")