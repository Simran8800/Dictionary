# dict1={"name":"raju", "marks":56}
# a=input("enter the input :-")
# if a in dict1.values():
#     print("exists")
# else:
#     print("not exists")
    

# my_dict = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
# }
# sum=0
# for i in my_dict:
#     sum=sum+my_dict[i]
# print(sum)
    
    
dic= {
  1: 'NAVGURUKUL',
  2: 'IN',  
  3:{
    'A' : 'WELCOME',
    'B' : 'To',
    'C' : 'DHARAMSALA'
}
}
for i in dic:
    if type(dic[i])== type(dic):
            for j in dic[i]:
                    del dic[i][j]
                    break
print(dic)






















