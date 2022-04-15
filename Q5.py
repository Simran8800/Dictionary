list1=['one','two','three','four','five','six']
list2=[1,2,3,4,5,6]
d={}
for i in range(len(list1)):
    d.update({list1[i]:list2[i]})
print(d)

