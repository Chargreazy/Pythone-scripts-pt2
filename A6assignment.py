print("#----------------------------------------------------------------------")
print("# Name:	        Antoine Fox                                             ")
print("# Date:	                                                              ")
print("# Reference:	Chapter 6, geeksforgeeks(for getIntegers), stackOverflow(for the list operations), and toppr")
print("# Title:	A6Assignment                                                ")
print("# Inputs:	Odd or even numbers                        ")
print("# Process:	Calculate if the number is divisible by 2 and/or 3                    ")
print("# Outputs:	The numbers divisible by 2 and 3, then None for those that arent at all   ")
print("#----------------------------------------------------------------------")

#The only way I could perform the operations correctly was through list comprehension


#Enter any odd oreven number followed by a space
getIntegers = [int(num) for num in input("Please enter however many numbers, each followed by a SPACE : ").split()]

#Calculates first if number is divisible by 2
divByTwo = [num for num in getIntegers if num % 2 == 0 ]

#Calculates first if number is divisible by 3
divByThree = [num for num in getIntegers if num % 3 == 0 ]

#Prints none for numbers divisible by none of them
divByNone = [num for num in getIntegers if num % 2 != 0 and num % 3 != 0]

#This function prints the results on which numbers were divisible by 2 or 3
def showResults(first,second, third, fourth):
    print("The number/s:", first,"were prompted")
    print("The number/s:",second, "are all divisible by 2")
    print("The number/s:", third, "are all divisible by 3")
    print("The number/s:", fourth, "arent divisible by neither 2 or 3")

#Prints none for numbers divisible by none of them
showResults(getIntegers, divByTwo, divByThree, divByNone)
