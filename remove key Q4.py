dic= {1: 'NAVGURUKUL',
2: 'IN',  
3:{'A' : 'WELCOME',
'B' : 'To',
'C' : 'DHARAMSALA'},
4:"hi",
5:{1:"dfgh",2:"dfghdfgh"}
}
for i in dic:
    if type(dic[i])== type(dic):
            for j in dic[i]:
                    del dic[i][j]
                    break
print(dic)

