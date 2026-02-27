numList=["all"]
evenList=["even"]
oddList=["odd"]
for i in range(1,51):
    numList.append(i)
    if i%2!=0:
        oddList.append(i)
    else:
        evenList.append(i)
print(numList)
print(evenList)
print(oddList)