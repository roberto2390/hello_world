#Roberto Rodrigues
#10/27/2020
#I seen that the code was missing a ":"
#also it was missing the userinput or call the function



#This code returns some mad libs text based on the user input
#Is the code always returnin the correct input?
#What do you think I did to write this code that I shouldn't have done?
adjective = input(" Write one of the following adjectives\n 'red, lazy, energetice, happy, or sad':")

def change_name(adjective):
    if adjective == 'red':
        return print("The quick brown fox jumps over the red dog")
    elif adjective == 'lazy':
        return print("The quick brown fox jumps over the lazy dog")
    elif adjective == 'energetic':
        return print("The quick brown fox jumps over the energetic dog")
    elif adjective == 'happy':
        return print("The quick brown fox jumps over the happy dog")
    elif adjective == 'sad':
        return print("The quick brown fox jumps over the happy dog")
    else:
        return print("No case for that adjective found!")
    
change_name(adjective)
