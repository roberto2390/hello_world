#Roberto Rodriguez
#11/4/2020
# Main Room to the game.
import Player_File as pf
import Section1 as p1

import Moster_file as mstr
import HealthCheck as HC
player = pf.playerinfo()
M1 = mstr.moster1
M2 = mstr.moster2
print("Welcome to the game.")
player.playername = input("\nWhat do I call you? ") 

print('\n Alright, lets start!', player.playername )

def movement():
    print("You are in your room.")
     #playerinfo/start

    Move = input("Leave room? press Y For yes N for No: ").upper()
    if Move == "N":
        movement()
        
    elif Move == "Y":
        print("\nYou are in the hallway")
        def hallway():
            Mover =input("Where to now?:\nType one[\"bedroom(B), parentsroom(P), staircase(S)\"]: ").upper()

            if Mover == "B":
                print("\nYou are back in your room")
                print("There is nothing in here\n")
                movement()
            elif Mover == "P":
                print("\nYou are in your parents room")
               
                def proom():
                    iteam = "Chips"
                    if iteam not in player.playertools :
                        print("There is a bag of chips on the bed!")  
                        action=input("Take the chips?:Type Y for yes N for no: ").upper()
                        if action == "Y":
                            player.playertools.append(iteam)
                            print("\nYou now have chips to gain health!")
                            proom() 
                        elif action == "N":
                            print("Okay, leave and come back if you change your mind.")
                            leave=input("leave room?: Type \"Y\" for yes \"N\" for no: ").upper()
                            if leave == "Y":
                                print("You are back in the hallway")
                                hallway()
                            elif leave == "N":
                                proom()
                            else:
                                print("Invalid input")
                                proom()
                        else:
                            print("Invalid Input")
                            proom()
                    else:
                        print("The room is empty")
                        leave=input("leave room?: Type \"Y\" for yes \"N\" for no: ").upper()
                        if leave == "Y":
                            print("\nYou are back in the hallway")
                            hallway()
                        elif leave == "N":
                            proom()
                        else:
                            print("\nInvalid input")
                            proom()
                proom()
            elif Mover == "S":
                print("You are at the staircase")
                def fight():
                    if M1.health > 0:
                        print("\nThere is a Lava monster!")   
                        fight1 = input("Do you want to fight or run back ?Type \"Y\" for yes \"R\" to RUN!!: ").upper()
                        if fight1 == "Y":
                            print("\nYou are fighting")#place fight AKA section 1
                            p1.fight()
                            HC.healthcheck()
                        elif fight1 == "R":
                            print("You are going back\n")
                            hallway()   
                        else:
                            print("Invalid input")
                            fight()
                    elif M1.health == 0:
                        print("\n The starecase is empty.")
                fight()
                def movingagain():
                    Move = input("\nWhere to now?: Type H for hallway, L for Living room, or S to stay: ").upper()
                    if Move == "H":
                        print("\n Going back")
                        hallway()
                    elif Move == "L":
                        print("You are in the living room")
                        print("Nothing is in here ")
                        Next = input("Where to now?")
                    elif Move == "S":
                        print("\nYou are still at the staricase")
                        movingagain()
                    else:
                        print("Invalid Input")
                        movingagain()

                movingagain()
            else: 
                print("Invalid Input\n")
                hallway()
        hallway()

    else:
        print("Invalid Input")
        movement() 
movement()





