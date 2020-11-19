#Roberto Rodriguez
#11/4/2020
#This is for the first part of the game.

import random as r
import Player_File as pf

def phase1():
    print(" Lets get you up to date. \n Your home has been invaded by elemental monsters, \n and your goal is to defeat each unique monster")
    start=input(" Ready? Type Y to contine or N to restart")


    
    if start == "Y":
       monster1()
    elif start == "N":
       print("Restart")
    return

def monster1():
    print("You are in your room on the second floor, and you have to make it to the backyard. \n The first monster down the hall is made up of lava!!! ")
    print("You are face to face now!!!")
    attack = r.randint(1,11)
    damage = int(pf.playerlife - attack ) 
    print("You are hit with lava leaving your health at", damage)

    return

     

    
