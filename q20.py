n=int(input())
y=int(input())
res=0
for i in range(y,n+1):
    if n%i==0:
        while i:
            res+=i%10
            i=i//10
        break
print(res)