#Reverse Lookup

def reverse_lookup(dict, value):
    keys = []
    
    for key in dict: #The key will be used to look up a value.
        if dict[key] == value: #If there's a key/value match, 
            keys.append(key) #the key will be append to the list.
    
    return keys
    

#English to Swahili Dictionary
engswahili = {
             "Kwaheri" : "Goodbye", "Salamu" : "Greetings", 
             "Hapana" : "No", "Ndio" : "Yes", 
             "Usiku Mwema" : "Goodnight", "Kitabu" : "Book",
             "Bafuni" : "Bathroom", "Kitanda" : "Bed"
             }


print("The Swahili phrase for Goodnight is ", reverse_lookup(engswahili, "Goodnight"))
print("The Swahili word for bathroom is ", reverse_lookup(engswahili, "Bathroom"))