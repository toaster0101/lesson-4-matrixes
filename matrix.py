import random
matrix=[]
#print(matrix)
#print(len(matrix))
#print(len(matrix[0]))
#print(matrix[1][2])
for i in range(9):
    m=[]
    for j in range(10):
        x=random.randint(10,99)
        m.append(x)
    matrix.append(m)
for i in range(10):
    for j in range(10):
        print(matrix[i][j],end=" ")
    print()