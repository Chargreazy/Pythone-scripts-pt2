print("""
#-----------------------------------------------------------------------
# Name:         Antoine Fox
# Reference:    Chapter 8    page # 335  problem # 1
# Title:        A8 assignment Program
# Inputs:       User enters which state either virginia, ohio and/or florida to input their statistics
# Process:      Loop through array/list to calculate total sales/week
# Outputs:      Print which the state and their pot sales as entered and whether or not its valid
#-----------------------------------------------------------------------
""")

import numpy as np

empID = ["PDQ545", "RMP865", "ATX139", "KFC511", "JCC877", "WTL223", "YOU412"]

#except backwards if input isnt valid
#Throw try/except modules for 1 and 2, use while loops with AND
#write comments over each module to describe it's purpose
def main():  
    weekly = weeklyHrsWorked()
    second = payRate()
    gross = grossPay(weekly, second)
    fedTax = fedTaxWheld(gross)
    stateTax = stateTaxWheld(grossPay)

def weeklyHrsWorked():
    worked = []
    
    for hours in range(7):
        work = int(input("Enter number of hours worked for each employee:"))
        if work < 50:
            worked.append(work)
    print("The number of hours each employee has worked this week is as listed:")
    print(np.array((empID, worked)))
    print("--------------------------------------------------------------------")
    return worked

##Edit input prompts
#each bit of data corresponds to each other
def payRate():
    rate = []
    weeklyHrs = 0
    
    while weeklyHrs < len(empID):
        try:
            weeklyHrs = int(input("Enter the pay rate for each employee:"))
        except ValueError:
            try:
                if weeklyHrs != str(weeklyHrs):
                    print("Error not integer,", end="")
                elif weeklyHrs < 25:
                    print("Error not possible,", end="")
                else:
                    pass
            except ValueError:
                continue
            splitLine = hours.split(": ")
            rate = [empID, weeklyHrs]
    print(rate)
    return weeklyHrs


def grossPay(hours, rate):
    gross = []
    pay = np.multiply(hours, rate)
    gross.append(pay)
    print("The gross pay for each of these employees is as listed:")
    print(empID)
    print(gross)
    print("-------------------------------------------------------------")
    return pay


def fedTaxWheld(newGross):
    Amount = []
    newGross = newGross * .15
    Amount.append(newGross)
    print("The federal tax of 15% withheld from each employee this week as listed:")
    print("--------", empID)
    print("In order:",newGross)
    print("-------------------------------------------------------------------")
    return Amount

def stateTaxWheld(finGross):
    Amount = []
    finGross = finGross * .08
    Amount.append(finGross)
    print("The state tax of 8% withheld from each employee this week as listed:")
    print("-------", empID)
    print("In order",finGross)
    print("-----------------------------------------------------------------")
    return Amount

main()
#clean up code
#fix title & references
