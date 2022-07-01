import random

# generate password based on 3 random letters, numbers, special character
#    1. generate 3 numbers, add to password string | password = 123
#    2. generate 3 letters, add to password string |  password = password + abc
#    3. generate 1 special character, add to password string | password = password + !

numberlist = [1,2,3,4,5,6,7,8,9]
specialcharslist = ["!","@","#","$","%","&"]
letterslist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def generator():
    password = ""
    numbers = random.choices(numberlist, k=3)
    letters = random.choices(letterslist, k=3)
    specialchar = random.choice(specialcharslist)

    for num in numbers:
        password = password + str(num)
        
    for letter in letters:
        password = password + str(letter)

    password = password + specialchar

    print(password)

generator()