num= {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69,'t':300}
max=0
for i in num:
    if num[i]>max:
        max=num[i]
        s=i
print(max,s)
max1=0
for i in num:
    if num[i]>max1:
        if max!=num[i]:
            max1=num[i]
            s=i
print(max1,s)
max2=0
for i in num:
    if num[i]>max2:
        if max!=num[i] and max1!=num[i]:
            max2=num[i]
            s=i
print(max2,s)