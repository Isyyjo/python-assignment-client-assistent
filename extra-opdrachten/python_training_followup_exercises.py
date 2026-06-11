# ============================================================
# PYTHON TRAINING - PRACTICE AFTER FUNCTIONS
# ============================================================

# In this training you will practice:
# - editing lists with append(), remove() and len()
# - expanding and updating dictionaries
# - combining functions with lists and dictionaries
# - using input()
#
# Tip:
# First read the assignment.
# Then write your code below the assignment.
# Test your code often by running the file.


# ============================================================
# PART 1 - EDITING LISTS
# ============================================================

# A list can store multiple values.
# You can add items with .append()
# You can remove items with .remove()
# You can count items with len()


# ------------------------------------------------------------
# Assignment 1
# ------------------------------------------------------------

# Create a list called animals with two animals.
animals = ["dog", "cat"]

# Add a third animal with .append()
animals.append("lemur")

# Print the list.
for animal in animals:
    print(animal)

# ------------------------------------------------------------
# Assignment 2
# ------------------------------------------------------------

# Create a list called cities with three cities.
cities = ["Amsterdam", "Italy", "Paris"]

# Remove one city with .remove()
cities.remove("Italy")

# Print the list.
for city in cities:
    print(city)


# ------------------------------------------------------------
# Assignment 3
# ------------------------------------------------------------

# Create a list called shopping_list with four items.
shopping_list = ["eggs", "banana", "tomatoes", "deoderant"]

# Print how many items are in the list.
print(f"You have {len(shopping_list)} items on your shopping list.")

# Example output:
# You have 4 items on your shopping list.



# ------------------------------------------------------------
# Assignment 4
# ------------------------------------------------------------

# Create a list called friends with three names.
friends = ["Dennis", "Frank", "Koen"]

# Add one name.
friends.append("Tom")

# Remove one name.
friends.remove("Koen")

# Print the full list.
for friend in friends:
    print(friend)

# Print how many friends are in the list.
print(f"You have {len(friends)} friends. Sad :(")

# ============================================================
# PART 2 - EXPANDING AND UPDATING DICTIONARIES
# ============================================================

# A dictionary stores information with keys and values.
# You can:
# - get a value
# - update a value
# - add a new key and value


# ------------------------------------------------------------
# Assignment 5
# ------------------------------------------------------------

# Create a dictionary called book.
# It should have:
# - title
# - author
# - pages
book = {
    "title": "The Gunslinger",
    "author": "Stephen King",
    "pages": 336
}


# Print the title of the book.
print(book["title"])


# ------------------------------------------------------------
# Assignment 6
# ------------------------------------------------------------

# Create a dictionary called phone.
# It should have:
# - brand
# - model
# - price
phone = {
    "brand": "Apple",
    "model": "Iphone 15",
    "price": 689
}

# Change the price.
phone["price"] = 300
# Print the dictionary.
print(phone)


# ------------------------------------------------------------
# Assignment 7
# ------------------------------------------------------------

# Create a dictionary called movie.
# It should have:
# - title
# - year
movie = {
    "title": "Whiplash",
    "year": "2014"
}

# Add a new key called genre.
movie["genre"] = "drama"

# Print the dictionary.
print(movie)


# ------------------------------------------------------------
# Assignment 8
# ------------------------------------------------------------

# Create a dictionary called profile.
# It should have:
# - name
# - age
# - city
profile = {
    "name": "Ismaël",
    "age": "24",
    "city": "Almere"
}

# Change the city.
profile["city"] = "Amsterdam"

# Add a key called hobbies with a list of two hobbies.
profile["hobbies"] = ["coding", "gaming"]

# Print the full profile.
print(profile)


# ============================================================
# PART 3 - FUNCTIONS WITH LISTS
# ============================================================

# A function can receive a list as a parameter.
# Inside the function you can loop through the list.


# ------------------------------------------------------------
# Assignment 9
# ------------------------------------------------------------

# Create a function called print_animals.
# The function gets one parameter: animals.
# The function prints each animal.
def print_animals(animals):
    for animal in animals:
        print(animal)

# Create a list with three animals.
animals = ["dog", "cat", "parrot"]

# Call the function with your list.
print_animals(animals)


# ------------------------------------------------------------
# Assignment 10
# ------------------------------------------------------------

# Create a function called count_items.
# The function gets one parameter: items.
# The function returns the number of items in the list.
def count_items(items):
    return len(items)

# Create a list with four items.
items = ["gun", "coin", "pickup", "xp"]

# Call the function.
number_of_items = count_items(items)

# Print the result.
print(number_of_items)

# ------------------------------------------------------------
# Assignment 11
# ------------------------------------------------------------

# Create a function called show_passed_grades.
# The function gets one parameter: grades.
# The function loops through the grades.
# If a grade is 6 or higher, print:
# Passed: 7
def show_passed_grades(grades):
    for grade in grades:
        if grade >= 6:
            print(f"You passed! Passing grade: {grade}")
        else:
            continue
    
# Create a list with at least five grades.
grades = [8, 6, 4, 7, 2]

# Call the function.
show_passed_grades(grades)


# ============================================================
# PART 4 - FUNCTIONS WITH DICTIONARIES
# ============================================================

# A function can also receive a dictionary.
# This is useful when one object has multiple pieces of information.


# ------------------------------------------------------------
# Assignment 12
# ------------------------------------------------------------

# Create a function called show_movie.
# The function gets one parameter: movie.
# The function prints:
# Title: ...
# Year: ...
# Genre: ...
def show_movie(movie):
    print(f"Title: {movie["title"]}")
    print(f"Year: {movie["year"]}")
    print(f"Genre: {movie["genre"]}")

# Create a dictionary for a movie.
movie = {
    "title": "Dunkirk",
    "year": "2017",
    "genre": "Action"
}
# Call the function.
show_movie(movie)


# ------------------------------------------------------------
# Assignment 13
# ------------------------------------------------------------

# Create a function called update_score.
# The function gets one parameter: player.
# Inside the function, add 10 to the player's score.
def update_score(player):
    player["score"] += 10

# Create a dictionary called player with:
# - name
# - score
player = {
    "name": "Issyjo",
    "score":  410
}

# Call the function.
update_score(player)

# Print the player dictionary.
print(player)


# ------------------------------------------------------------
# Assignment 14
# ------------------------------------------------------------

# Create a function called print_profile.
# The function gets one parameter: profile.
# The profile dictionary has:
# - name
# - age
# - hobbies
profile = {
    "name": "John Tinder",
     "age": 21,
     "hobbies": ["long walks on the beach", "reading", "poetry"]
}

def print_profile(profile):
    print(f"{profile["name"]}, {profile["age"]}")
    for hobby in profile["hobbies"]:
        print(hobby) 

# The function should print the name and age.
# Then it should loop through the hobbies and print each hobby.
print_profile(profile)


# ============================================================
# PART 5 - INPUT
# ============================================================

# input() lets the user type something.
# The value from input() is always a string.
# If you need a number, use int().


# ------------------------------------------------------------
# Assignment 15
# ------------------------------------------------------------

# Ask the user for their name.
username = input("Hello, user! Please state your name: ")

# Print:
# Welcome, ...
print(f"Welcome, {username}!")


# ------------------------------------------------------------
# Assignment 16
# ------------------------------------------------------------

# Ask the user for their age.
age = input("Please state your age: ")
user_age = float(age)

# Check whether the user is 18 or older.
# Print whether the user is an adult or underage.
if user_age >= 18:
    print("You are an adult.")
elif user_age <= 4:
    print("You are a baby!")
elif user_age <= 18:
    print("You are underage. You child...")
else:
    print("How are you alive?")



# ------------------------------------------------------------
# Assignment 17
# ------------------------------------------------------------

# Ask the user for a hobby.
# Add the hobby to a list called hobbies.
# Print the list.



# ------------------------------------------------------------
# Assignment 18
# ------------------------------------------------------------

# Create a function called greet_user.
# The function gets one parameter: name.
# The function prints:
# Hello, ...
#
# Ask the user for their name with input().
# Call the function with the name.



# ------------------------------------------------------------
# Assignment 19
# ------------------------------------------------------------

# Create a dictionary called user.
# Ask the user for:
# - name
# - city
#
# Store both answers in the dictionary.
# Print the dictionary.



# ============================================================
# EXTRA CHALLENGE
# ============================================================

# Create an empty list called tasks.
# Ask the user for three tasks.
# Add each task to the list.
# Print:
# You have 3 tasks:
# Then print each task on a new line.



# ============================================================
# END
# ============================================================

# If you can do this, you can:
# - edit lists
# - update dictionaries
# - use functions with lists
# - use functions with dictionaries
# - use input in simple programs