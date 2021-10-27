import math

def nickname():
    print("Let's create your nickname!")
    grades = ["Freshman", "Sophomore", "Junior", "Senior"]

    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    grade = ""
    isValid = False
    while not(isValid):
        grade = int(input("Enter your grade (9-12): "))
        if 9 <= grade <= 12:
            isValid = True
        else:
            isValid = False
        
      
    grade = int(grade)

    nickname = firstName[:math.ceil(len(firstName)/4)] + lastName[:math.ceil(len(lastName)/2)]
    nickname += " the " + grades[grade-9]
    print("Your auto-generated nickname is: " + nickname)
    
    

nickname()

# not finished
def nicknameZodiac():
    print("Let's create your nickname!")
    grades = ["Freshman", "Sophomore", "Junior", "Senior"]
    # blah didn't finish this

    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    birthYear = int(input("Enter your birth year: "))
    
    grade = ""
    isValid = False
    while not(isValid):
        grade = int(input("Enter your grade (9-12): "))
        if 9 <= grade <= 12:
            isValid = True
        else:
            isValid = False
        
      
    grade = int(grade)

    nickname = firstName[:math.ceil(len(firstName)/4)] + lastName[:math.ceil(len(lastName)/2)]
    nickname += " the " + grades[grade-9]
    print("Your auto-generated nickname is: " + nickname)

