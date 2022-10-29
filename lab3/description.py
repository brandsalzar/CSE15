from logic import TruthTable

propList = []
meaningList = []
end_it = False
#while loop takes in your propositions
while not end_it:
    propVar = raw_input("Enter a proposition:")
    propList.append(propVar)
    more_it = raw_input("Would you like to enter more?(Y/N):")
    if more_it == 'N':
        end_it = True
#generate the truth table
propTable = TruthTable(propList)
#check for consistency
consistent = False
for i in range(len(propTable.table )):
    if propTable.table[i][1] == [1]*len(propList):# prints [1,1]double check it
        consistent = True
        break

if consistent == True:
    #print out my variables
    print("Your program uses propositional variables " + str(propTable.vars))
    #for loop it for the number of variables and meaning storage
    for i in range(len(propTable.vars)):
        meaning = raw_input("Enter the meaning of " + propTable.vars[i] + ": ")
        meaningList.append(meaning)
    #gives instances for the times when there is consistency
    print("Your description is consistent when:")
    #if statement checking for the "is" and "not"
    for i in meaningList:
        if (propTable.table[0][0] != propTable.table[0][1]):#mess around with the
            print("It is not the case that " + i)
        else:
            print("It is the case that " + i)
else:
    print('They are not consistent')
