def dic():
    numr=int(input("Enter range:"))
    a=[]
    print("Prime numbers:",end=' ')
    for n in range(1,numr):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            a.append(n) 
    # print(a)
    i=0
    c={}
    while i<len(a):
        k=i
        v=a[i]
        i+=1
        c.update({k:v})
    print(c)
dic()