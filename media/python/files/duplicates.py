#Avoid Duplicates


print("Enter a list of words; press the enter button twice to finish>>")

words = []#List

while True:#Collects words from the user.
    word = input()
    
    if word not in words:#If the word entered doesn't already exist in the list, append it to the list.
       words.append(word)
 
    if word == "":
        break

words.remove(words[-1])#Removes the blank space from the list.

print(words)