''' Elections 

You are the head of the election committee in your village. Each Political party is associated 
with a unique number and the votes are represented as an integer array A. where each 
element contains the party number voted for by the villagers. For a party to win, they must 
have a majority of votes. our task is to find and return an integer value denoting the winning 
party's number. Return -1 if there is no party with a majority. 
Note: If only one vote is there he is the winner. 
Input Format : input1: An integer value representing the number the 
number of voters input2: An integer array A representing the votes of the 
voters. output Format: 
Return an integer value denoting the winning party's number.Return -1 there is no party 
with a majority 
Example 1:

Input:
6 
1 1 2 2 2 3 Output:
2 

Explanation:
As 2 got the most number of votes i.e 3. 
Example 2:

Input:
6 1 2 1 1 2 
2 

Output:
-1 
Explanation:
As both the contestants got same votes there is no majority'''

n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
       d[i]+=1
    else:
      d[i]=1 
lis=list(d.items())
lis.sort(reverse=True,key=lambda x:x[1]) 
if len(lis)==1:
    print(l[0][0])
else:
    if lis[0][1]==lis[1][1]:
        print(-1)
    else:
        print(lis[0][0])   

