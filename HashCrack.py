from hashlib import md5

passHash = input("Enter password hash:")

wordList = open("LeakedPasswords.txt","r")

def hashCrack(passHash):
    for word in wordList:
        word = word.strip()
        print(word,"word in for loop")
        guess = md5(word.encode("utf-8"))
        print(guess.hexdigest(),"digest")

        if guess.hexdigest() == passHash:
            print("Password Found")
            print("Password is " + word)
            break
        else:
            print("password not found")
hashCrack(passHash)
