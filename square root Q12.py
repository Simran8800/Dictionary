dic=int(input("enter the number"))
x={}
i=1
while i<=dic:
    a=i*i
    x.update({i:a})
    i=i+1
print(x)
