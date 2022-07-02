#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
def lordofunction():
    ### HELPER FUNCTIONS (IF NECESSARY) ###
    special_characters = """!@#$%^&*()-+?_=,<>/"""
    def lengthCheck(passwd):
        if len(passwd) < 8:
            print("Ensure password is at least 8 characters long")
        else:
            print("password is good length") #more specific, ie 8-11 characters weak, 12-14 moderate, 15+ strong

    def specialCharCheck(passwd):
        if any(char in special_characters for char in passwd):
            print("has special characters")
        else:
            print("doesn't have special characters")
    ### MAIN FUNCTION ###

    def main():
        passwd = sys.argv[1]
        lengthCheck(passwd)
        specialCharCheck(passwd)
        print(passwd)
    main()
 

  


