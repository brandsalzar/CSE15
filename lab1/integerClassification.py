#Type casts the string entered into an integer
number = int( raw_input("Enter an even or odd number:"))
#if statement checking to see if a real number was entered
if number == 0:
    print "Zero is not EVEN or ODD"
else:
    eveOdd = number%2 #New variable getting the remainder
    if eveOdd == 0:   #If-Else checking the remainder to classify it as an ODD or and Even number
        print "EVEN"
    else:
        print "ODD"
