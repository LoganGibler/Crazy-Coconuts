
import re
import sys


def timeCrack():
    crack_speed = 20000000000 #default assumed rate 
    entropy = 0
    passwd = input("Password to time estimate:")

    passwd_len = len(passwd)

    policies = { 'Uppercase characters': 0,
                 'Lowercase characters': 0,
                 'Special characters': 0,
                 'Numbers': 0
               }
    entropies = { 'Uppercase characters': 26,
                 'Lowercase characters': 26,
                 'Special characters': 33,
                 'Numbers': 10
               }
            
    for char in passwd:
        if re.match("[\[\] !\"#$%&'()*+,-./:;<=>?@\\^_`{|}~]", char):
            policies["Special characters"] += 1
        elif re.match("[a-z]",char):
            policies["Lowercase characters"] += 1
        elif re.match("[A-Z]",char):
            policies["Uppercase characters"] += 1
        elif re.match("[0-9]",char):
            policies["Numbers"] += 1
    for policy in policies.keys():
    
        if policies[policy] > 0:
            entropy += entropies[policy]
    print(entropy,"entropy")
    print(policies,"policies")
    time_ = "minutes"
    speed = ((entropy**passwd_len) / crack_speed) / 60 # seconds in hour
    
    if speed > 60:
        speed = speed / 60
        time_ = "hour"

    if speed > 24:
        speed = speed / 24
        time_ = "days"

    if speed > 365:
        speed = speed / 365
        time_ = "years"

    if time_ == "years" and speed > 100:
        speed = speed/ 100
        time_ = "centuries"

    if time_ == "centuries" and speed > 1000:
        speed = speed / 1000
        time_ = "millennia"
    if int(speed) < .01:
        print("Time to crack password: {:,.9f} {}".format(speed, time_))
    if int(speed) > .01:
        print("Time to crack password: {:,.2f} {}".format(speed, time_))
timeCrack()

    
        