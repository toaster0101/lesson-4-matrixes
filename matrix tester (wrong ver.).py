matrix=[]
for i in range(9):
    entry=int(input("here "))
    matrix.append(entry)
for i in range(9):
    x=" "
    if (i+1)%3==0:
        x="\n"
    print(matrix[i],end=x)
if matrix[0]==matrix[4]and matrix[8]:
    print("yes")
else:
    print("no")