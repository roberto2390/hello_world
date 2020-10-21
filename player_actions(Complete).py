#player_actions.py


def check_play_again(user_input):
    #Your code here
    #gave the user an option to between Y' and N'
     if user_input == "Y":
         print("Good luck!") 
     
     elif user_input == "N":
         print("Quiting Game")
    #if the user gives an input other than
    # Y' or N' they are told that it's an invalid input  
     else :
         print("wrong input")
               

check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
