#Roberto Rodriguez
#10/27/2020
#at first, this should of flipped the actions because in means if they are
#the same print "go away, pirate." 
#why say go away from when you logged in.

#This program will take a password from the user and print an appropriate message
#The 'in' keyword checks to see if a value exists somewhere in the given string.

greeting = input("Hello, possible pirate! What's the password?")
if greeting in ("Arrr!"):
	print(" Greetings, hater of pirates!")
else:
        print("Go away, pirate. ")
