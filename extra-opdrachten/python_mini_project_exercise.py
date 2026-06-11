# ============================================================
# PYTHON MINI PROJECT - STUDENT MANAGER
# ============================================================

# In this mini project you will build a small student manager.
#
# You will practice:
# - lists
# - dictionaries
# - functions
# - input()
# - if/else
# - for-loops
#
# Goal:
# Create students, store them in a list, and show useful information.


# ============================================================
# PART 1 - CREATE ONE STUDENT
# ============================================================

# Assignment 1
#
# Create a dictionary called student.
# student = {}

# Ask the user for:
# - name
# - age
# - city
# Store the answers in the dictionary.
# print("Please state your name: ")
# student["name"] = input()

# print("Please state your age: ")
# student["age"] = input()

# print("What city do you live in? ")
# student["city"] = input()

# Print the dictionary.
# print(student)


# ============================================================
# PART 2 - CREATE A FUNCTION
# ============================================================

# Assignment 2
#
# Create a function called create_student.
# The function asks the user for:
# - name
# - age
# - city
def create_student():
    print("Welcome new student!")
    print("Please enter your name: ")
    name = input()
    print("Please enter your age: ")
    age = input()
    print("What city do you live in? ")
    city = input()

    # The function creates a dictionary with that information.
    student = {
            "name": name,
            "age": age,
            "city": city
        }
    
    # The function returns the dictionary.
    return student

# Call the function once.
# Store the result in a variable.
# student1 = create_student()

# Print the result.
# print(student1)


# ============================================================
# PART 3 - STORE MULTIPLE STUDENTS
# ============================================================

# Assignment 3
#
# Create an empty list called students.
students = []

# Use the create_student function three times.
# Add every student to the students list with .append()
students.append(create_student())
students.append(create_student())
students.append(create_student())

# Print the full students list.
# print("Student List: ")
# for student in students:
#     print(f"Name: {student["name"]}")
#     print(f"Age: {student["age"]}")
#     print(f"City: {student["city"]}")


# ============================================================
# PART 4 - SHOW STUDENTS CLEARLY
# ============================================================

# Assignment 4
#
# Create a function called show_students.
# The function gets one parameter: students.
# The function loops through the list.
# For every student, print:
#
# Name: ...
# Age: ...
# City: ...
# ----------
def show_students(students):
    print(" ")
    print("Student List: ")
    print("---------------")
    for student in students:
        print(f"Name: {student["name"]}")
        print(f"Age: {student["age"]}")
        print(f"City: {student["city"]}")
        print("---------------")

show_students(students)
# ============================================================
# PART 5 - CHECK ADULT OR UNDERAGE
# ============================================================

# Assignment 5
#
# Create a function called check_age.
# The function gets one parameter: student.
# If the student is 18 or older, print:
# Mila is an adult
#
# Else print:
# Mila is underage
def check_age(student):
    if float(student["age"]) >= 18 and float(student["age"]) <= 100:
        print(f"{student["name"]} is an adult.")
    elif float(student["age"]) <= 18 and float(student["age"]) >= 1:
        print(f"{student["name"]} is underage.")
    else:
        print(f"{student["name"]} shouldn't be alive")

# Then loop through the students list and call check_age for each student.
for student in students:
    check_age(student)


# ============================================================
# PART 6 - EXTRA CHALLENGE
# ============================================================

# Assignment 6
#
# Create a function called count_adults.
# The function gets one parameter: students.
# The function returns the number of adult students.
#
# Print:
# Number of adult students: ...



# ============================================================
# END RESULT
# ============================================================

# Your program should be able to:
# - create students with input
# - store students in a list
# - print students clearly
# - check who is adult or underage
# - count the adult students
