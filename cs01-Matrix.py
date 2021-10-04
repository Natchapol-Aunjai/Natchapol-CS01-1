import numpy as np
MatrixOne = []
MatrixTwo = []
loop = 1 
MatrixColumns = int(input('EnterYourColumns : '))
MatrixRows = int(input("EnterYourRows : "))
while(loop <= 2):
    print("EnterYourMatrix",loop)
    for i in range(MatrixRows) :
        for j in range(MatrixColumns) :
            print("MatrixColumns [",i,",",j,"] :",end ="")
            if(loop == 1):
                MatrixOneInput = int(input(""))
                MatrixOne.append(MatrixOneInput)
        else:
            MatrixTwoInput = int(input("")) 
            MatrixTwo.append(MatrixTwoInput)
    loop += 1
NumpyMatrixOne = np.asarray(MatrixOne)
NumpyMatrixTwo = np.asarray(MatrixTwo)
NewMatrixOne=NumpyMatrixOne.reshape(MatrixRows,MatrixColumns)
NewMatrixTwo=NumpyMatrixTwo.reshape(MatrixRows,MatrixColumns)
print(NewMatrixOne,"\n=========================")
print(NewMatrixTwo,"\n=========================")
sum = np.add(NewMatrixOne, NewMatrixTwo)
print(sum)

MatrixRows,MatrixColumns = [int(i) for i in input().split()]
MatrixOne = []
MatrixTwo = []
for Matrix1 in range(MatrixRows):
    Maxtrix1 = [int(i) for i in input().split]
    MatrixOne.append(Matrix1)
for Matrix2 in range(MatrixRows):
    Matrix2 = [int(j) for j in input().split()]
    MatrixTwo.append(Matrix2)
print()
for i in range(MatrixRows):
    for j in range(MatrixColumns):
        print(MatrixOne[i][j] + MatrixTwo[i][j],end = "")
        print()