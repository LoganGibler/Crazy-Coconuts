from hashlib import md5, sha1, sha224, sha256, sha384, sha512



def hashCrack():
    passHash = input("Enter password hash:")
    wordList = open("LeakedPasswords.txt","r")
    count = 0

    if len(passHash) == 128:
        print("Hash type: SHA512")
    elif len(passHash) == 96:
        print("Hash type: SHA384")
    elif len(passHash) == 64:
        print("Hash type: SHA256")
    elif len(passHash) == 40:
        print("Hash type: SHA1")
    elif len(passHash) == 32:
        print("Hash type: MD5")
    elif len(passHash) == 56:
        print("Hash type: SHA224")
    else:
        print("Could not detect hash type. :(")

    if len(passHash) == 32:
        for word in wordList:
            word = word.strip()
            guess = md5(word.encode("utf-8"))
            if guess.hexdigest() == passHash:
                print("Password is: " + word)
                count = 1
                break

    if len(passHash) == 64:
        for word in wordList:
            word = word.strip()
            guess = sha256(word.encode("utf-8")).hexdigest()
            if guess == passHash:
                print("Password is: " + word)
                count = 1
                break

    if len(passHash) == 40:
        for word in wordList:
            word = word.strip()
            guess = sha1(word.encode("utf-8")).hexdigest()
            if guess == passHash:
                print("Password is: " + word)
                count = 1
                break

    if len(passHash) == 96:
        for word in wordList:
            word = word.strip()
            guess = sha384(word.encode("utf-8")).hexdigest()
            if guess == passHash:
                print("Password is: " + word)
                count = 1
                break

    if len(passHash) == 56:
        for word in wordList:
            word = word.strip()
            guess = sha224(word.encode("utf-8")).hexdigest()
            if guess == passHash:
                print("Password is: " + word)
                count = 1
                break

    if len(passHash) == 128:
        for word in wordList:
            word = word.strip()
            guess = sha512(word.encode("utf-8")).hexdigest()
            if guess == passHash:
                print("Password is: " + word)
                count = 1
                break


    if count == 0:
        print("Password not found")

hashCrack()
