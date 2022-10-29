print "Enter 10 integers" #promts user to input their numbers
bigOdd = 0    #variable initialized to get the biggest Odd number
#for-loop running to 10 for the ten numbers inputed by user
for i in range(10):
    tenInts = int(raw_input())#inputs the ten numbers
    eveOdd = tenInts%2#Checks remainder for even or odd
#If-Else checking the value of eveOdd to determine if its odd and checks if the current odd number is bigger than the previous
    if eveOdd == 1 and bigOdd < tenInts:
        bigOdd = tenInts
#If-else checking for odd or even to see what statement will be printed
if (bigOdd%2) == 1:
    print "Largest odd number is", bigOdd
else:
    print "No odd numbers were entered"
