import random
import sys
# generate password based on 3 random letters, numbers, special character
#    1. generate 3 numbers, add to password string | password = 123
#    2. generate 3 letters, add to password string |  password = password + abc
#    3. generate 1 special character, add to password string | password = password + !

numberlist = ["1","2","3","4","5","6","7","8","9"]
specialcharslist = ["!","@","#","$","%","&"]
letterslist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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

special_characters = """!@#$%^&*()-+?_=,<>/"""
def passcheck(password):
    
    if len(password) < 8:
        print("Ensure password is at least 8 characters long")
    else:
        print("password is good length") #more specific, ie 8-11 characters weak, 12-14 moderate, 15+ strong

    
    if any(char in special_characters for char in password):
        print("has special characters")
    else:
        print("doesn't have special characters")

def main():
    passwd = ""
    option = sys.argv[1]
    # if option:
    #     print("Please give option")

    if option == "generate":
        generator()
    if option == "check":
        passwd = sys.argv[2]
        print("Checked Password:  ", passwd)
        passcheck(passwd)
    if option == "generatecheck":
        passcheck(generator())
        
main()