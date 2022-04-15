n=int(input("enter the no"))
a={}
i=1
while i<=n:
    key=i
    Value=i*i*i
    a.update({key:Value})
    i=i+1
print(a)

 
