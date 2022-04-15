dic={'ishu':10,'bijender':45,'foo':33,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print(dic)
