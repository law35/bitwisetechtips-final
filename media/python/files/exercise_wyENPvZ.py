#Average 
#====================================================================#

values = [] #create an empty list

while True:
    val = int(input("Enter the numbers to average; enter 0 to quit."))
    values.append(val) #This will add each number to the values list.
    
    if val == 0: #if the user enters 0, the program will end.
        break
        
newlist = values[:-1] #This will remove the 0 from values.
   
print(sum(newlist) / len(newlist)) #The sum of the newlist divided by its length.