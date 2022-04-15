from heapq import nlargest


my_dict = {'a':56, 'b':58, 'c':50,'d':40, 'e':100, 'f':200}
h= nlargest(2, my_dict, key = my_dict.get)
for val in h:
    print(val, ":", my_dict.get(val))





# my_dict = {'A': 67, 'B': 23, 'C': 45,
#            'D': 56, 'E': 12, 'F': 69}
# k=[]
# k = Counter(my_dict)
# high = k.most_common(3)
# for i in high:
#     print(i[0]," :",i[1])
