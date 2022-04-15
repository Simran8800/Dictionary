# list=[{},{},{}]

# my_list1 = [{1,2},{},{}]
# print(all(not d for d in list))
# print(all(not d for d in my_list1))


l = [{},{},{}] 
all_empty = True
for i in l:
  if i:
    all_empty = False

print (all_empty)