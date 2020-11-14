#Roberto Rodriguez
#11/12/2020
#This prints 10 random intenger between 25 and 35
import random as r


    
num= 0
Max= 10
while  num  <  Max:
    r.randint(25,35)
    num +=1
    if num > 0:
        print(r.randint(25,35),num)

