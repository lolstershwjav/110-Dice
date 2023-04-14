import time
import random

user = input("Do You Want To Roll A Dice (y/n): ")



while(user.upper()=="Y"):
    no = random.randint(1,6)
    print ("["+f'{no}'+"]")
    user = input("Do You Want To Roll A Dice (y/n): ")


