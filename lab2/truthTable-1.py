from logic import TruthTable

propX = raw_input("Enter proposition 1: ")
propY = raw_input("Enter proposition 2: ")

tableOne = TruthTable(['p','q'], [propX])
tableTwo = TruthTable(['p', 'q'], [propY])

if(tableOne.table == tableTwo.table):
	print("The Propositions are equivalent")
else:
	print("The propositions are not equivalent")
