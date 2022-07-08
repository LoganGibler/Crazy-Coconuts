from hashlib import md5

passHash = input("Enter password hash:")

wordList = open("LeakedPasswords.txt","r")

def hashCrack(passHash):
    count = 0
    for word in wordList:
        word = word.strip()
        # print(word,"word in for loop")
        guess = md5(word.encode("utf-8"))
        # print(guess.hexdigest(),"digest")

        if guess.hexdigest() == passHash:
            print("Password Found")
            print("Password is " + word)
            count += 1
        
    if count == 0:
        print("Password not found")
hashCrack(passHash)
