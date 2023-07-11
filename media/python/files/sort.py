#Sort in order

print("Enter numbers only; enter a 0 when done>>")

integers = []#List

while True:#Collects integers from the user until the user enters zero.
    integer = int(input())
    integers.append(integer)
    
    if integer == 0:
        break
   
integers.remove(integers[-1])#Removes the last integer from the list.

print("Unsorted:", integers)

integers.sort()#The sort()function will sort the numbers in numerical order.
print("Sorted:", integers)