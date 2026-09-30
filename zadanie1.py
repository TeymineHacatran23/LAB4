from math import*
s=0
for n in range(1, 51):
  t=(((pi/3)**(2*n+1))/(factorial(n+1)))*cos(n)
  s=s+t
print(s)
  