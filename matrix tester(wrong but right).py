matrix=[]
for i in range(9):
    entry=int(input("here "))
    matrix.append(entry)
for i in range(9):
    x=" "
    if (i+1)%3==0:
        x="\n"
    print(matrix[i],end=x)
if matrix[1]and matrix[2]and matrix[3]and matrix[5]and matrix[6]and matrix[7]==0 and matrix[0]and matrix[4]and matrix[8]!=0:
    print("yes")
else:
    print("no")