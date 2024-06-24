def func():
   try:
      l = [1,2,3,4]
      i = int(input("enter the indexs: "))
      print(l[i])
      return 1
   except:
      print("some error occured")
      return 0
   finally:
      print("this will always execute")
# print("this will always execute")

x = func()
print(x)    