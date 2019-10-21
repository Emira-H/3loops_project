theString = "je suis - pas +"

if "-" in theString:
    i=0
    while "-" in theString:
        if theString[i] == '-':
            break
        i+=1
        theString = theString[:i]+'\_'+theString[i+2: