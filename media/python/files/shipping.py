#Shipping Calculator

print("Enter items; Type q to quit.")
items = []#Use a list to store the items.
    
while True:
    item = input()#Takes the items from user input.
    items.append(item)#Add each item to the items[] list.
    if item == "q":#If the user enters q, the program will calculate and finish.
        break

items.remove(items[-1])#This removes the "q" from the items[] list.
items.remove(items[0])#Removes the first item in the list; this item will not factor in the final calculation.



def shipping_sum(items):
    ship_total = 10.95#A constant value for the first item, which was removed at line 13.
    
    for i in items:
        ship_total = ship_total + 2.95#Will add 2.95 to the running total.
    
    print("Shipping Total = ", "${:,.2f}".format(round(ship_total, 2)))
    
shipping_sum(items)