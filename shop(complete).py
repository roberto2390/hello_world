#shop.py


def check_money(total_cost, customer_money):
    #Your code here
    if total_cost < customer_money:
        print("You have enough to pay")
        # when the user has enough money
    else :
        print("You dont have enough money to pay")
        #when the user doesn't have enough money
    return total_cost < customer_money
#To return True or False

#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
