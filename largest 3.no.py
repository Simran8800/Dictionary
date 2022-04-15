dic={'I_1':45.50,'I_2':35,"I_3":41.30,'I_4':55,'I_5':24}
max=1
for i in dic:
    if dic[i]>max:
        max=dic[i]
        s=i
print(max)
max_1=1
for i in dic:
    if dic[i]>max_1:
        if max!=dic[i]:
            max_1=dic[i]
            s=i
print(max_1)
max_2=1
for i in dic:
    if dic[i]>max_2:
        if max!=dic[i] and max_1!=dic[i]:
            max_2=dic[i]
            s=i
print(max_2)