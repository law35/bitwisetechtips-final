#Average

print("Enter numbers only; enter a 0 when done>>")

integers = []#List

while True:#Collects integers from the user until the user enters zero.
    integer = int(input())
    integers.append(integer)
    
    if integer == 0:
        break
   
integers.remove(integers[-1])#Removes the last integer from the list.


def avg(integers):
    total = 0#Will store the total
    
    for i in integers:#Each value in the list will be added to the total.
       total = total + i
        
    print("Grade average =", total / len(integers))#Will print the total divided by the number of integers in the list.

avg(integers)