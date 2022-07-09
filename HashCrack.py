from hashlib import md5



def hashCrack():
    passHash = input("Enter password hash:")
    wordList = open("LeakedPasswords.txt","r")
    count = 0

    for word in wordList:
        word = word.strip()
        guess = md5(word.encode("utf-8"))
        print(guess.hexdigest())
        if guess.hexdigest() == passHash:
            print("Password is: " + word)
            count = 1
            break
           
    if count == 0:
        print("Password not found")

hashCrack()
