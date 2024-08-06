n = int(input())
h=[]
matrixA=[]
matrixB=[]
matrixC=[]
for i in range (1,n+1):
  for j in range(1,n+1):
    h.append(0)
  matrixC.append(h)
  h=[]
print(matrixC)
for i in range(n):
  row = [ ]
  for x in input().split(','):
    row.append(int(x))
  matrixA.append(row)

for i in range(n):
  row = [ ]
  for x in input().split(','):
    row.append(int(x))
  matrixB.append(row)
for i in range(n):
  for j in range(n):
    for k in range(n):
       matrixC[i][j]=matrixC[i][j]+(matrixA[i][k]*matrixB[k][j])
print(matrixC)
for i in range(n):
  for j in range(n):
    if(j!=n-1):
      print(matrixC[i][j],end=",")
    else:
      print(matrixC[i][j])