
dic=[
  {"first":"1"}, 
  {"second": "2"}, 
  {"third": "1"}, 
  {"four": "5"}, 
  {"five":"5"}, 
  {"six":"9"},
  {"seven":"7"},
  {"ten":"10"}
]
i=0
b={}
c=[]
while i<len(dic):
      b.update(dic[i])
      i=i+1
for i in b.values():
      if i not in c:
            c.append(i)
print(c)
