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
student1 = create_student()

# Print the result.
print(student1)


# ============================================================
# PART 3 - STORE MULTIPLE STUDENTS
# ============================================================

# Assignment 3
#
# Create an empty list called students.
# Use the create_student function three times.
# Add every student to the students list with .append()
# Print the full students list.



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
#
# Then loop through the students list and call check_age for each student.



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
