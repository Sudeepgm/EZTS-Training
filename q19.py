l=list(map(int,input().split()))
target=int(input())
l.sort()
res=0
for k in range(len(l)-2):
    i=k+1
    j=len(l)-1
    while i<j:
        prod=l[i]*l[j]*l[k]
        if prod<target:i+=1
        elif prod>target:j-=1
        else:res+=1;i+=1;j-=1
print(res)

       