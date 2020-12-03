#Roberto Rodriguez
#11/4/2020
#This is for the first part of the game.

import random as r
import Player_File as pf
import Moster_file as mf
M1=mf.moster1

ph = pf.playerinfo
#if fight this is the fighting and 

#also the this imports the monsters

def fight():
   if M1.health > 0:
      print("The monsters health is at", M1.health)
      a = input("quicly what do you pick up around you to fight?[Watergun(W),fireextinguisher(f),plan(P)]: ").upper()
      if a == "W":
         print("That didn't kill it!")
         print("The monster hit back! Your health is now at", ph.playerlife - M1.attack )
         M1.health - ph.hit2
         fight()

      if a == "F":
         print("That killed the monster! No damage taken")
         M1.health - ph.hit1
         fight()

      if a == "P":
         print("That didn't kill it!")
         print("The monster hit back! Your health is now at", ph.playerlife - M1.attack )
         M1.health - ph.hit2
         fight()


      else:
         print("Invalid Input")
         fight()



   else:
      print("\nMoster is already dead")
   





     

    