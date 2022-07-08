from hashlib import md5

passHash = input("Enter password hash:")

wordList = open("rockyou_clean.txt","r")

def hashCrack(passHash):
    count = 0
    for word in wordList:
        word = word.strip()
        guess = md5(word.encode("utf-8"))
        if guess.hexdigest() == passHash:
            print("Password " + word)
            count += 1
        
    if count == 0:
        print("Password not found")
hashCrack(passHash)
