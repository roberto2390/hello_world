#Roberto Rodriguez
#11/12/2020
#This lets the user shoot his arrow in a competion. if the user shoots and gets the random 0,
#  they get no points, and get to keep the arrow.
#if they shoot a an get random 10 they get 20 points.
import random as r
  
myscore = []
maxarws = 10
noarws = 0
total = 0
while noarws < maxarws:
    print("Score Card: ", myscore)
    print("Total:", total)
    print("You have ",maxarws,"arrows left.")
    shoot = input("Type \"S\" to shoot arrow: ").upper()
    #This lets the machine know if the user typed in the right key.
    #if not they get redirected to shoot again.
    if shoot == 'S':
        points=r.randint(0,10)
    #tells the machinie what to output depending on the type of point the
    #user gets.
        if points == 0:
            print("\nZero points! No arrows taken.\n")
            myscore.append(points)

        
        elif points == 10:
            myscore.append(20)
            print("\nBullseye!",points*2, "points!\n")
            maxarws -=1
            total +=20

        else:
            print("\nYou got",points, "points\n ")
            myscore.append(points)
            maxarws -=1
            total += points

    else: 
        print("\nWrong input! \n ")         
#when the user is done playing they get all their stats.
print("Nice job!\nScore card:", myscore, "\nTotal points:", total, '\n')

    
