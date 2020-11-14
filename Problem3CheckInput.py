#Roberto Rodriguez
#11/12/2020
#This checks if the user input is the letter A, B, or C. 
# The loop should continue until a valid input is entered by the user.

#Bounus .upper() was added to accept if the users input was lowercase

answer=["A", "B", "C"]
response=""

while  response not in answer :
    response = str(input("Type one of the following[\'A\', \'B\', or \'C\': ")).upper()
    
else:
    print("Thats right!") 





