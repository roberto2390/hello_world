#named the function

def track_skip():
    #asked the user for current track
    current_track = int(input("what track are you on?: "))
    # asked the user how many tracks they 
    skip_count = int(input(" How many tracks would you like to skip?: "))
#added the current track to the number of tracks the user
    #wanted to skip
    skip_result = current_track + skip_count
    #printed the user what track they are going to
    print(" You are skipping to track ", skip_result)
    #asked the user again to see if they want to skip again
    return track_skip()
track_skip()
