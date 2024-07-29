s=input().lower()
v='aeiou'
max=0
vowel=''
for i in v:
    if s.count(i)>max:
        max=s.count(i)
        vowel=i
print(vowel)