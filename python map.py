# MAP

# def cube(x):
#     return x*x*x
# print(cube(3))

# l =[2,3,4,3,5]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

# # newl = list(map(cube,l))
# newl = list(map(lambda x :x*x*x,l))
# print(newl)

# # FILTER
# def function_filter(a):
#     return a>3

# newnewl = list(filter(function_filter , l))
# print(newnewl)

from functools import reduce
def mysum(x,y):
    return x+y
l= [2, 3, 4, 5]
sum = reduce(mysum , l)
# sum = reduce(lambda x, y :x+y , l)
print(sum)