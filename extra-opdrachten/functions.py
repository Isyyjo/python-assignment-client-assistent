# Opdracht: herhaling verwijderen met functies
#
# De code hieronder werkt, maar is nog niet netjes opgebouwd.
# Er staan meerdere stukken code in die sterk op elkaar lijken of zelfs
# precies hetzelfde doen.
#
# Jouw opdracht is om deze herhaling te verminderen door eigen functies
# te maken.
#
# Kijk vooral naar stukken code die:
#
# - meerdere keren terugkomen
# - één duidelijke taak hebben
# - de hoofdcode onnodig lang maken
#
# Maak van zulke stukken code een functie met een duidelijke naam.
# Daarna roep je die functie aan op de plekken waar de herhaalde code stond.
#
# Denk bijvoorbeeld aan een functie die:
#
# - alle studenten toont
# - een studentnummer omzet naar een index
# - misschien later een student aanmaakt of aanpast
#
# Begin met de grootste herhaling.
# In deze code is dat het tonen van de studentenlijst.
#
# Stappen:
#
# 1. Lees de code en zoek welk blok code meerdere keren voorkomt.
# 2. Bedenk wat dat blok code doet.
# 3. Geef die taak een duidelijke functienaam.
# 4. Zet het herhaalde blok in een functie.
# 5. Vervang de herhaalde blokken in de while-loop door een functie-aanroep.
# 6. Test of het programma nog steeds hetzelfde werkt.
#
# Het doel is niet om nieuwe functionaliteit toe te voegen.
# Het doel is dat de code korter, duidelijker en makkelijker aan te passen wordt.
#
# Als je klaar bent, zou je hoofdprogramma minder herhaling moeten bevatten.
# De losse functies doen dan elk één duidelijke taak.

students = [
    {"name": "Anna", "age": 20, "active": True},
    {"name": "Bram", "age": 22, "active": True},
    {"name": "Carlos", "age": 21, "active": False},
]

# FUNCTION DEFINITIONS

# print lijst met studenten
def show_students():
    print("----- STUDENTS -----")
    for index, student in enumerate(students):
        name = student["name"]
        age = student["age"]
        active = student["active"]

        if active:
                status = "active"
        else:
                status = "inactive"

        row = f"{index + 1}. {name} - {age} years old - {status}"
        print(row)

    print("--------------------")

# voeg een student toe aan lijst
def add_student():
    name = input("Name: ")
    age = int(input("Age: "))

    student = {
            "name": name,
            "age": age,
            "active": True,
        }

    students.append(student)

# wijzig de gegevens van een student
def edit_students():
    number = int(input("Student number: "))
    index = number - 1

    name = input("New name: ")
    age = int(input("New age: "))

    students[index]["name"] = name
    students[index]["age"] = age

# zet status van student op "inactive"
def deactivate_student():
    number = int(input("Student number: "))
    index = number - 1

    students[index]["active"] = False
     

#PROGRAM
while True:
    user_action = input("Type show, add, edit, deactivate or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("show"):
        show_students()

    elif user_action.startswith("add"):
        add_student()
        show_students()

    elif user_action.startswith("edit"):
        edit_students()
        show_students()

    elif user_action.startswith("deactivate"):
        deactivate_student()
        show_students()

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Bye!")
