#Mean, Mode and Median
#=====================================================================#
import statistics

numbers = [] #create an empty list

while True:
    num = int(input("Enter 4 or more numbers; enter 0 to quit."))
    numbers.append(num) #This will add each number to the numbers list.
    
    if num == 0: #if the user enters 0, the program will end.
        break
        
newlist = numbers[:-1] #This will remove the 0 from numbers list.
   
print("Mean =", statistics.mean(newlist), 
    "Median =", statistics.median(newlist), 
    "Mode =", statistics.mode(newlist))