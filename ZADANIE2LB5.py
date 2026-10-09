n=int(input())
a=list(map(int, input().split()))
c=0
for i in range(n-2):
    if a[i]+a[i+2]==2*a[i+1]:
        c+=1
print(c)