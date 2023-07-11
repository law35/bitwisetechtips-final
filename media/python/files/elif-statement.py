#elif-statement 

x = 15
y = 20
z = y - x

if x == 20 and y == 20:
    print(x + y)
elif x == 15 and y == 20:
    print(z)
elif x == 20 and y == 15:
    print("x is not 20 and y is not 15, this will never print out.")
    
if z == 5:
    print("Yes, y - x = 5.")
    
if y % x == 0:
    print("You're kidding me right?")
elif x == 15 and y == 20:
    print("x is 15 and y is 20.")
    