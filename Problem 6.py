# Question 6 : Given a list of numbers,
#  Iterate it and print only those numbers which are divisible of 5

def find_Dividable(numberList):
    for num in numberList:
        if (num % 5 == 0):
            print(num)

numList = [10,20,30,40,50,44,22,14,23,96]
find_Dividable(numList)