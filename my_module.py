#Roberto Rodriguez
#11/5/2020
#This is the file that with the functions.
import random as r
import math as m

def function1():
    print("This is function 1")
    for i in range(1,11):
        print(r.randint(25,35))

    return

def function2():
    print("This is function 2")
    list=['a','b','c','d','e','x','y','z']
    print("This is the list",list)
    print(r.choice(list))

    return

def function3():
    print('This is finction 3')
    odd = r.randrange(1,101,2)
    print(odd)
    return


def function4():
    print("This is function 4")
    A = int(input("A: "))
    B = int(input("B: "))
    Answer = m.sqrt(A**2 + B**2)
    print(round(Answer,2))
    return


