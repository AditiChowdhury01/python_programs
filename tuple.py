# tup = (1 , 5 , 6 , 7 , 8 )
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[-1])

# if 4 in tup:
#     print("yes")

# tup2 = tup[1:4]s
# print(tup2)

# tuple1 = [1,3,5,2,1,1,75]
# res = tuple1.count(1)
# res = tuple1.index(1)
# print(res)

countries = ('a','b' ,'c', 'j')
temp = list(countries)
temp.append("f")  
temp.pop(3)
temp[1] = "d"
countries = tuple(temp)
print(countries)