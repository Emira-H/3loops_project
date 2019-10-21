theString = "je suis - pas +"

print(theString)
if "-" in theString:
    i=0
    while "-" in theString:
        if theString[i] == '-':
            break
        i+=1
        theString = theString[:i]+'\_'+theString[i+2]
print(theString)
