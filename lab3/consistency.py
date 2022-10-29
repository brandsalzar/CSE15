from logic import TruthTable

propList = []
end_it = False

while not end_it:
    propVar = raw_input("Enter a proposition:")
    propList.append(propVar)
    more_it = raw_input("Would you like to enter more?(Y/N):")
    if more_it == 'N':
        end_it = True

propTable = TruthTable(propList)

consistent = False
for i in range(len(propTable.table )):
    if propTable.table[i][1] == [1]*len(propList):# double check it
        consistent = True
        break

if consistent:
    print('They are consistent')
else:
    print('They are not consistent')

propTable.display()

#propTable.display()
#print(propTable.table)
#row print(propTable.table[0])
#column propTable.table[0][1] )
#value at index print(t)
#print(propTable.table[1])
#print(propTable.table[1][0], propTable.table[1][1])

#or i in propList:#can't traverse table
#s    if (propTable.table[][] == propTable.table[][]): #how can I traverse the table rows?



#if(table.table == table.table):
#    print("Your description is consistent")

# propList = [" ", " ", " ", ""]
#*propList = []

#propList.append('p and q')

#while != 'N':#for i in range(x):#for i in range(x):
#    propVar = raw_input("Enter a proposition: \n")#prop[i] = raw_input("Enter a proposition: \n")
#    propList.insert(i, propVar)
#    print(propList[i])#for j in prop:
#    more = raw_input("Would you like to enter more (Y/N): \n")
#    if (more == 'Y'):
#        propList.insert( (i +1) , "")
#        x = len(propList)
#        continue
#    elif (more == 'N'):
#        print("insert the consistency function here")
#        break
        #fruits.append("orange")
        #prop.insert(i,prop)
#for i in range(1000):
#    print(propList[i])



#tableOne = TruthTable(['p','q'], [prop])

#if(tableOne.table == tableTwo.table):
#	print("Your description is consistent.")
#else:
#	print("Your description is NOT consistent.")
