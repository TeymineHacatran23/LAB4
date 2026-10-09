from math import*
n=int(input())
nam=[]
for i in range(n):
  nam.append(int(input()))
c=0
for i in range(len(n)-1):
  if abs(nam[i]-nam[i+1])<=5:
    c+=1
print(c)
