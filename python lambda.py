# def double(x):
#     return x
def appl(fx , value):
    return 6 + fx(value)

double = lambda x :x*2
cube = lambda x :x*x*x
avg = lambda x,y,z :(x+ y + z)/3

print(double(4))
print(cube(3))
print(avg(2,3,6))
print(appl(lambda x:x*x , 2))
print(appl(cube , 2))