

#named the function
def BMI_calc():
    #asked the user for height
    height = int(input("what is your height in inches?: "))
    #asked the user for weight
    weight = int(input(" what is your weight in lbs?: "))
    #made a variable for using the weight and height in the BMI calc.
    results = float(weight / height ** 2 *(703))
    #returned the reults to the user, also made sure to round to the last
    #decimal place
    print(round(results,2), "is your BMI.")
    #asked the user again.
    return BMI_calc()
BMI_calc()
