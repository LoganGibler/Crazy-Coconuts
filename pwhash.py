#!/usr/bin/env python3
# Hash Function
# SHA hash algorithms.
import hashlib
def hash_pw():
# initializing string
    str = input("Password to hash: ")
# encoding str using SHA1
    result = hashlib.sha1(str.encode())
# printing the equivalent hexadecimal value.
    print(str + " hashed to SHA1 is: ")
    print(result.hexdigest())
# encoding str using SHA224()
    result = hashlib.sha224(str.encode())
# printing the equivalent hexadecimal value.
    print(str + " hashed to SHA224 is: ")
    print(result.hexdigest())
# encoding str using SHA256()
    result = hashlib.sha256(str.encode())
# printing the equivalent hexadecimal value.
    print(str + " hashed to SHA256 is: ")
    print(result.hexdigest())
# initializing string
    str = str
# encoding str using SHA384()
    result = hashlib.sha384(str.encode())
# printing the equivalent hexadecimal value.
    print(str + " hashed to SHA384 is: ")
    print(result.hexdigest())
# # initializing string
# str = str
# initializing string
    str = str
# encoding str using SHA512()
    result = hashlib.sha512(str.encode())
# printing the equivalent hexadecimal value.
    print(str + " hashed to SHA512 is: ")
    print(result.hexdigest())
hash_pw()