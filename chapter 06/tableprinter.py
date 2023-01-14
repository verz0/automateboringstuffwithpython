def printTable(tableData):
   colWidths = [0] * len(tableData)
   for i in range (len(tableData)):
      l=[]
      for j in range (len(tableData[i])):
         l.append(len(tableData[i][j]))
      colWidths[i] = (max(l))
      
   for i in range (len(tableData[0])):
      for j in range (len(tableData)):
         print(tableData[j][i].rjust(colWidths[j]), end=' ')
      print()
      
tableData = [['apples', 'orangessssss', 'banananananana', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)