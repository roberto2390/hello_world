
#gave a nmae to the function
def interior_angle_calc():
#gave a title to the user for what this is.
    print("Interior angles of a regular polygon calculator")
#asked for the user to give a number of sides
    num_sides = int(input("How many sides?: "))
# named a varibale results where the users input goes through the formula
    results = int(180 * (num_sides - 2) / num_sides)
#returned the answer to the user
    print("Answer: ", results)
#for the user can in put another number of angles
    return interior_angle_calc()
#called the function
interior_angle_calc()
                
