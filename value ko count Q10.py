dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
sum=0
for i in dict1:
   sum=sum+len(dict1[i])
print(sum)

