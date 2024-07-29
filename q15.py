''' Finding commas

Liam works as a data analyst for a company that stores massive amounts of numerical data. He has been 
tasked with determining how many commas are used when writing numbers in the range of 1 to N 
(inclusive) in a specific format 
In this format, if numbers are more than four digits long, commas are used to separate the numbers into 
groups of three, starting from the right for the representation of the number. Your task is to help Liam find 
and return an integer value, representing the total number of commas used when writing each integer in the 
range of 1 to N 

Input Specification: 
Input: An integer value N. representing the number range. 

Output Specification: 
Return an integer value, representing total number of commas used when writing each integer in the range 
of 1 to N. 

Sample Input:
5000 

Sample Output:
4001'''

n=int(input())
res=0
cur=1000
comma=1
while cur<=n:
    next=cur*1000
    nums=min(n-cur+1,next-cur)
    res+=nums*comma
    cur=next
    comma+=1
print(res)