from math import*
p=1
for n in range(1,16):
  s=((n**(0.75*n))/factorial(n+1))*log(n+1)
  p=p*s
print(p)