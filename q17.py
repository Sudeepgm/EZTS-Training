''' Best Grade 

Andrew has a string N consisting of lowercase English letters representing respective grades of N students 
in his class. His grade is at Pth index. He can swap any two adjacent grades. 
Your task is to help Andrew find and return a string value, representing maximized grade by bringing 
lexicographically smallest character on the Pth index after doing at most K swaps 

Sample Input:
abcdefg 
3 
2 

Sample Output:
a'''

s=input('enter the string:')
p=int(input('enter the position:'))
k=int(input('enter the swaping value:'))
start=max(0,p-k-1)
end=min(len(s),p+k)
print(min(list(s[start:end])))
