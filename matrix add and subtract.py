matrixA=[[1,2],[3,4]]
matrixB=[[5,6],[7,8]]
matrixC=[]
matrixCA=[]
matrixCB=[]
n=0
for i in range(4):
    if i==2:
        n=0
    if i>=2:
        matrixCB.append(matrixA[0][n]+matrixB[0][n])
    else:
        matrixCA.append(matrixA[1][n]+matrixB[1][n])
    n+=1
matrixC.append(matrixCB)
matrixC.append(matrixCA)
for i in range(2):
    for j in range(2):
        print(matrixC[i][j],end=" ")
    print()