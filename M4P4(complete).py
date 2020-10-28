#Roberto Rodriguez
#10/27/2020
# the only issue I found was that if the year was above 2020
#it wouldnt say that it was the past
#gave it a range, but I am not sure if there was a better method 


# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's--- > already made.
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))
r= range(1900, 2021)
if year <= 1900:
    print ("Woah, that's the past!")
elif year in r:
    print ("That's totally the present!")
else :
    print ("Far out, that's the future!!")
