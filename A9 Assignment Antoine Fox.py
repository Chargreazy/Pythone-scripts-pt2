#-------------------------------------#)
#Name: Antoine Fox)
#Date: 4/04/24)
#Reference: Assignment 1b for CISP 300)
#Title: Customer info update)
#Inputs: the inches of rain for each month
#Process: inches of rain, with there respective months
#Outputs: 3 months with the most and least amount of rain, sum of the inches of rain,
#The amount in inches of rain with the month it's associated with
#-------------------------------------#



#Main module
def main():
    rainfall = calcRainfall()
    print(rainfall)
    print("----------------------------------------------------------------------------------------------------------")
    sorte = sortInches(rainfall)
    print("The months with the least amount of rainfall were the months with,",sorte[0], sorte[1], "and the month with", sorte[2],"inches!")
    print("----------------------------------------------------------------------------------------------------------")
    print("The months with the most amount of rainfall were the months with, ",sorte[11], sorte[10], "and the month with", sorte[9],"inches!")
    print("----------------------------------------------------------------------------------------------------------")


#Module calculates all the rainfall(in inches) together in order of month
def calcRainfall():
    rainAmts = []
    inches = []
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    str1 = ""
    
    for i in range(len(month)):
        rain = float(input(f"Enter the number of inches of rain for the month of {month[i]}:"))
        inches.append(rain)
        values = month[i]+ " "+"which has"+" "+ str(inches[i])
        statement = tuple("The month of"+" "+values + " " + "inches of rain")
        rainAmts.append(statement)
        rainAmts[i] = list(rainAmts[i])
        rainAmts[i] = str1.join(rainAmts[i])
        fall = str(rainAmts[i])
        total = sum(inches)
    print("----------------------------------------------------------------------------------------------------------")
    print("The total amount of rainfall was",total,"inches this year")
    print("----------------------------------------------------------------------------------------------------------")
    return rainAmts

#Module sorts the previous modules rainfall inches for each month in ascending order
def sortInches(rainfall):
    
    rainTotals = []
    str2 = ""
    
    #once split into integers, let it bubble sort
    for o in range(len(rainfall)):
        rainfall[o] = list(rainfall[o])
        integer = rainfall[o][27:-15]
        intString = str2.join(integer)
        number = float(intString)
        rainTotals.append(number)
        date = rainfall[o][13:-27]
        month = str2.join(date)
        
    n = len(rainTotals)
    #bubble sorting algorithm
    for j in range(0, n-1):
        swapped = False
        for i in range(0, n-j-1):
            if rainTotals[i]>rainTotals[i+1]:
                swapped = True
                rainTotals[i], rainTotals[i+1] = rainTotals[i+1], rainTotals[i]

        if not swapped:
            return rainTotals

main()
