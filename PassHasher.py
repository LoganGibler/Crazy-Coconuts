from hashlib import md5
import sys

passhash = sys.argv[1]
wordList = open("LeakedPasswords.txt", "r")

def passHasher():
    count = 0
    for word in wordList:
        word = word.strip()
        guess = md5(word.encode())
        if guess.hexdigest() == passhash:
            print("Password Found: " + word)
            count += count
        

passHasher()