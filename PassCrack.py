#!/usr/bin/env python3

import sys
#main objective of script is to compare to rockyou.txt to see if password is compromised

#grab a wordlist we would want to run against password
#Stretch – search for partial matches, loose matches

def compare_list(rockyou):
    rockyou_list = " "
    password = " "
    rockyou.sort()

#for loop needs to run every line in file to compare to password
#   for line in rockyou():
    if password in list:
        return "Password already exist"
         
    else:
        return "Password is acceptable" 

def main():
    file_name = sys.argv
    opened_file = open(file_name)
    print(compare_list(opened_file))
    opened_file.close()

  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()