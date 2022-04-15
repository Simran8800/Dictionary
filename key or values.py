from multiprocessing.sharedctypes import Value


a={'2':4,'5':6,'8':9}
b={}
for x,y in a.items():
    b.update({y:x})
print(b)
    