from logic import TruthTable

myTable = TruthTable(['p', 'q'], ['p -> q', '-p or q'])
myTable.display()
myTable.latex()