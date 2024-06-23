n = int(input("enter the no.of elements:"))
l1 = []
for i in range (n):
    l1.append(int(input("enter number")))
def num(l1):
    if len(l1)<3:
        return l[3]
    else:
     nums = set(l1)
     l = list(nums)
     l.sort()
     return( l[-3])

print(num(l1))