#After each fight this will check if the user wants to regain their health after a fight or while in the game
import Player_File as pf

foods = ['chips']
hlth = pf.playerinfo




def healthcheck():
    count = 0
    while hlth.playerlife != 100 and count <1:
        print("\nlooks like you lost some life. ")
        print("looks like you can check to see if you have some food stored in your tools.")
        answ=input("Type \"Y\" to check for food, \"N\" to keep going: ").upper()
        if answ == "Y":
            count +=1
            foods = 'chips'
            def check():
                
                if foods not in hlth.playertools:
                    print("\nSorry, You have nothing to eat.\n")#, hlth.playertools)
                else:
                    print("You can eat", hlth.playertools)
                    choice = input("Would you like to eat?\"Y\" for yes \"N\" for no: ").upper()
                    if choice == "Y":
                        results= 100 - hlth.playerlife 
                        hlth.playerlife += results
                        print("Your health is now at", hlth.playerlife)
                    elif choice == "N":
                        print("its here if you change your mind")
                        
                    else:
                        print("Invalid input")
                        check()
            check()
        if answ == "N":
            print("Alright check later")
            count +=1
            
#def healthcheck2():

