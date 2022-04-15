from heapq import nlargest


my_dict = {'a':56, 'b':58, 'c':50,'d':40, 'e':100, 'f':20}
a=nlargest(3,my_dict, key=my_dict.get)
print(a)