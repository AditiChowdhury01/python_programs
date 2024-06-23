a = input("who is the pm of india : ")
b = input("who is the presidentof india : ")
c = input("who was the first pm of india : ")
d = input("who was the  first president of india : ")
e = input("who is the cm of west bengal : ")
f = input("who is the governor of west bengal : ")
list = [a,b,c,d,e,f]
ans = ["narendra modi","draupadi murmu","pt. jawaharlal nehru","rajendra prasad","mamta banerjee","c v ananda bose"]
print("your first question answer is: ",a)
print("your second question answer is: ",b)
print("your third question answer is: ",c)
print("your fourth question answer is: ",d)
print("your fifth question answeris: ",e)
print("your sixth question answer is: ",f)
if(list ==ans):
    if (list[0] == ans[0]):
      print("you won 20000 rupees")
    if (list[1] == ans[1]):
      print("you won 40000 rupees")
      
    if (list[2] == ans[2]):
      print("you won 60000 rupees")
    
    if (list[3] == ans[3]):
      print("you won 100000 rupees")
      
    if (list[4] == ans[4]):
      print("you won 200000 rupees")
      
    if (list[5] == ans[5]):
      print("you won 400000 rupees")
    print("you won 400000 rupees")

else:
  print("you lost")