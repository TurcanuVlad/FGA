x=[[2,3,4,4,64],
  [2,69,64,5,12],
  [7,228,4,6,161],
  [8,420,9,666,10],
  [1,5,2,1,125]]



for i in range(len(x)):
    print("Suma elem",i+1,"=",sum(x[i]))

s=[]
for j in range(len(x[0])):
    c=[]
    s=[]
    for rind in x:
        c.append(rind[j])
    s.append(sum(c))
    print("suma elementelor din coloana:",j+1,"=",s)

s=[]
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i==j :
            s.append(x[i][j])
print("Diagonala principala=",s)
s=[]
for i in range(len(x)):
    for j in range(len(x[0])) :
        n=5
        if i+j==n-1:
            s.append(x[i][j])
print("Diagonala secundara=",s)