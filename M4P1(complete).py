#Roberto Rodriguez
#10/27/2020
# When code was Run no error appeared
#only things added was if the user went beyond 23 hours they went beyone the range 0-23



#This program takes the current time in hours between 0-23
#and the number of hours the user will wait.
#It will print what the time is in hours (between 0-23) after the user is done waiting
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt

if finalTimeInt >= 23:
    print("It is", finalTimeInt - 23, "The next day")
else:
    print(finalTimeInt)
