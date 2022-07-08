import random
import sys
import string
from hashlib import md5
# MAKE MAN PAGE, LIKE LEGIT OPTIONS MAN ex: -gc -c -g
#  STRETCH:  maybe script asks if u want the generated password checked
#encode
#passcrack
numberlist = string.digits
specialcharslist = ["!","@","#","$","%","&"]
letterslist = string.ascii_letters


def generator():
    password = ""
    passwordlist = []

    numbers = random.choices(numberlist, k=random.randint(3,6))
    letters = random.choices(letterslist, k=random.randint(3,6))
    specialchar = random.choice(specialcharslist)

    scramble = []
    for num in numbers:
        scramble.append(num)
    for letter in letters:
        scramble.append(letter)

    scramble.append(specialchar)
    
    passwordlist += random.choices(scramble, k=random.randint(10,16))
   
    passwordlist.insert(random.randint(0,10), specialchar)

    random.shuffle(passwordlist)

    for character in passwordlist:
        password += character

    print("Your generated password: ", password)
    return password
    # passcheckgenerator(password)

special_characters = """!@#$%^&*()-+?_=,<>/"""

def passcheckgenerator(password):
    uppercount = 0
    lowercount = 0
    print("Checked Password:  ", password)
    for letter in password:
        if letter in special_characters:
            continue
        if letter == letter.upper():
            uppercount += 1
        if letter == letter.lower():
            lowercount += 1
    if uppercount == 0:
            print("Password needs an uppercase letter")
    if lowercount == 0:
            print("Password needs a lowercase letter")
    
    if len(password) < 8:
        print("Ensure password is at least 8 characters long")
    else:
        print("Password has sufficient length ") #more specific, ie 8-11 characters weak, 12-14 moderate, 15+ strong

    
    if any(char in special_characters for char in password):
        print("Password has special characters")
    else:
        print("Needs at least 1-2 special characters")


def passcheck():
    password = input("Enter password to check: ")
    uppercount = 0
    lowercount = 0
    print("Checked Password:  ", password)
    for letter in password:
        if letter in special_characters:
            continue
        if letter == letter.upper():
            uppercount += 1
        if letter == letter.lower():
            lowercount += 1
    if uppercount == 0:
            print("Password needs an uppercase letter")
    if lowercount == 0:
            print("Password needs a lowercase letter")
    
    if len(password) < 8:
        print("Ensure password is at least 8 characters long")
    else:
        print("Password has sufficient length ") #more specific, ie 8-11 characters weak, 12-14 moderate, 15+ strong

    
    if any(char in special_characters for char in password):
        print("Password has special characters")
    else:
        print("Needs at least 1-2 special characters")

    
def compare():
    string1 = input("Enter password to search for: ")
    file1 = open("rockyou_clean.txt", "r")
    readfile = file1.read()
    if string1 in readfile:
        print('You chose -->',string1 + ".", '\nThis password is compromised. Please choose again.')
    else:
        print('You chose -->', string1 , '\nThis password was not found')
    file1.close()


def hashCrack():
    passHash = input("Enter password hash:")
    wordList = open("rockyou_clean.txt","r")
    count = 0
    
    for word in wordList:
        word = word.strip()
        guess = md5(word.encode("utf-8"))
        if guess.hexdigest() == passHash:
            print("Password " + word)
            count += 1
            break

    if count == 0:
        print("Password not found")


def main():
    option = sys.argv[1]
    if option == "--g":
        generator()
    if option == "--c":
        passcheck()
    if option == "--gc":
        password = generator()
        passcheckgenerator(password)
    if option == "--cp":
        compare()
    if option == "--ch":
        hashCrack()

main()