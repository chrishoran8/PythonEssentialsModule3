#basic board creation
###############################################################################
rowZero = []

#create a single row on a chessboard, with coordinates
for i in range(8):    
    rowZero.append("r0,c"+str(i))

print("row zero:")
print(rowZero)

#a quicker way to do this is list comprehension
#newlist = [expression for item in iterable if condition == True]
#in our case: 
#newlist = [expression for item in iterable]
rowOne = ["r1,c"+str(i) for i in range(8)]

print("row1")
print(rowOne)

rowTwo = ["r2,c"+str(i) for i in range(8)]
rowThree = ["r3,c"+str(i) for i in range(8)]
rowFour = ["r4,c"+str(i) for i in range(8)]
rowFive = ["r5,c"+str(i) for i in range(8)]
rowSix = ["r6,c"+str(i) for i in range(8)]
rowSeven = ["r7,c"+str(i) for i in range(8)]

#create a chess board, which will need 8 rows
basicBoard = []

#populate each element in the list with another list
#or in our case, popluate our chess board with eight rows
basicBoard.append(rowZero)
basicBoard.append(rowOne)
basicBoard.append(rowTwo)
basicBoard.append(rowThree)
basicBoard.append(rowFour)
basicBoard.append(rowFive)
basicBoard.append(rowSix)
basicBoard.append(rowSeven)

print("basic board printed row by row")
print(basicBoard[0])
print(basicBoard[1])
print(basicBoard[2])
print(basicBoard[3])
print("...getting board of typing now....")
print()

#printing out row by row gets boring fast..... how about a for loop??

print("basic board printed using for loop")
for i in range(8): #this is our 8 rows
    print(basicBoard[i])
print()  

#nestedForBoard
############################################################################### 
#crating row by row is not efficient
#we can nest it so it can be all done in a oner!

nestedForBoard = []

#populating a list with 8 rows
for i in range(8): #create our chess board which needs 8 rows
    tempRow = []#this tempRow is created 8 times
    for j in range(8):#within each tempRow, create 8 squares
        tempRow.append("r"+str(i)+",c"+str(j))
    nestedForBoard.append(tempRow)

print()
print("nested For loop board")
for i in range(8): #this is our 8 rows
    print(nestedForBoard[i])
print()
#nestedListComprehension
###############################################################################

#quickboard = create 8 squares inside 8 rows
#quickboard = [[create 8 Squares] create 8 rows ]
#quickboard = [[expression] for item in iterable]
quickBoard = [["r"+str(i)+",c"+str(j) for i in range(8)] for j in range(8)]

print("nested list comprehension board")
for i in range(8): #this is our 8 rows
    print(quickBoard[i])