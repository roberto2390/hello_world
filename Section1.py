#Roberto Rodriguez
#11/4/2020
#This is for the first part of the game.

import random as r
import Player_File as pf
import Moster_file as mf
import HealthCheck as HC
M1=mf.moster1

ph = pf.playerinfo
#if fight this is the fighting and 

#also the this imports the monsters

def fight():
   if M1.health > 0:
      print("\nThe monsters health is at", M1.health, ". Be careful it can take between 20-25 damage every hit.")
      a = input("quicly what do you pick up around you to fight?[Watergun(W),fireextinguisher(f),Mom's plant(M)]: ").upper()
      if a == "W":
         print("\nThat didn't kill it!")
         print("The monster hit back! Your health is now at", ph.playerlife - M1.attack )
         ph.playerlife -= M1.attack
         M1.health -= ph.hit2
         

      if a == "F":
         print("\nThat killed the monster! ")
         M1.health -= int(100)
         if ph.playerlife == int(100):
            print("No Damage Taken\n")
         else:
            print("You almost got taken out")
            print("Your health is now", ph.playerlife)

         

      if a == "M":
         print("\nThat didn't kill it!")
         print("The monster hit back! Your health is now at", ph.playerlife - M1.attack )
         ph.playerlife -= M1.attack
         M1.health -= ph.hit2
         
   

      else:
         print("Invalid Input")
         fight()



   HC.healthcheck      



   






     

    