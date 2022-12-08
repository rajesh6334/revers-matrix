#matrix formate2
n=int(input('enter no of rows'))
m=int(input('enter no coloumns'))
k=n*m
for i in range(1,n+1):
    for j in range(1,m+1):
        print(k,end=' ')
        k=k-1
    print()
