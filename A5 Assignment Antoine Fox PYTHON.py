print("""#--------------------------------------------------------------------------------------------#")
# Name:     Antoine Fox                                                                      #")
# Date      3/19/24                                                                          #")
# Title:    CISP 300 Assignment #5 py                                                        #")
# Reference: Try/except loops from various online sources                                                #")
# Inputs:   The amount of each expense, and your current hourly wage             #")
# Process:  Calculates total amount for number of expenses	                     ")
# Outputs:  How many hours total you need to work at your job	   ")
#--------------------------------------------------------------------------#""")

#DONE, MAKE COMMENTS AND DO FLOWCHART

#edit the output make it optional
import math
import numpy as np

total_hours = []

def main():
    ask = askAmount()
    total = calcAmount(ask)
    jam = math.ceil(total)
    print("The bare minimum number of hours needed to work, to cover the expenses is:",jam,"hours")
    print("...assuming there's no cash in the bank")

#use while loops with AND for try/except
#While the input doesnt equal 0, keep inputting the expense
#Any other input thats not above 0 will get try/excepted
#ONCE 0 IS INPUTTED YOU WILL GET YOUR TOTAL
#Zero ends the while loop
def askAmount():
    i = 0
    expense = -.01
#IT MAY TAKE A SECOND FOR THE LOOP TO CALL
    while expense != 0:
        try:
            expense = float(input("Please enter the amount(float) for each expense: "))
        except ValueError:
                 try:
                    if expense != str(expense):
                        print("Error not integer,", end="")
                    else:
                        pass
                 except ValueError:
                     continue
        total_hours.append(expense)
        i +=1
        if (i % 10) == 0:
            print(f"You have {i} expenses for the month")
    return total_hours
#Enter your current hourly wage in this module to calculate how many hours you need
def calcAmount(tot):
    tot = sum(tot)
    print(f"The total of all the expenses comes out to ${tot}")
    wage = float(input("Enter your current hourly wage amount: "))
    print("You currently make",wage,"$ an hour at your job")
    workHours = tot/wage
    return workHours


main()
