

def check_money(total_price, customer_money):
    missing_amount = total_price - customer_money
    change = total_price - customer_money
    if total_price < customer_money:
            print("You have enough to pay")
            print("Your chnage is ", "$" , change)
            print("Thank you for shopping")
            # when the user has enough money
    else :
            print("You dont have enough money to purchase")
            print("You need " , "$", missing_amount, "left to purchase")
            #when the user doesn't have enough money
    return total_price < customer_money
    #To return True or False





def check_out():
    #welcoming the user
    print("welcome")
    #asking the user how many of the selected item
    corn = float(input("How many pieces of corn do you want?: " ))
        #asking the user how many of the selected item

    peaches = float(input("How many peaches do you want?: " ))
        #asking the user how many of the selected item

    chicken = float(input("How many pieces of chicken do you want?: " ))
        #asking the user how many of the selected item

    total_price = corn * 2.00 + peaches * 1.00 + chicken * 3.00
    #adding the total of each iteam times the number of each iteam
    #from the user
    print("$", round(total_price, 2), " is your total")
    #rounding the results, aslo telling the user that this is their total
    #shop.py
    customer_money = int(input("How much money do you have?: "))
# This will make up the customer_money part
#of the function check_money(total_price, customer_money)
    
    check_money(total_price, customer_money)
    
    return check_out()
                    
check_out()
