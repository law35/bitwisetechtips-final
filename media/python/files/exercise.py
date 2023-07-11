#Compute Hypotenuse
#Formula to use: a2 + b2 = c2(a squared plus b squared equal c squared)

def hypotenuse():
    a = int(input("Enter side a value>> "))
    b = int(input("Enter side b value>> "))
    
    #We will use the pow()function to raise each input by the power of two. 
    sideA = pow(a, 2)
    sideB = pow(b, 2)
    
    #Compute and print the hypotenuse.
    c = sideA + sideB
    print(c)

#Call the function    
hypotenuse()