matrix=[]
flag=0
for i in range(3):
    tempList=[]
    for j in range(3):
        entry=int(input("here "))
        tempList.append(entry)
    matrix.append(tempList)
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
        if i==j:
            if matrix[i][j]!=0:
                flag+=1
        else:
            if matrix[i][j]==0:
                flag+=1
    print()
if flag==9:
    print("yes")
else:
    print("no")