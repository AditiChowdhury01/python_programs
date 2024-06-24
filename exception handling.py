a = input("enter the number: ")
print(f"the muliplication table of {a} is :")
try:
    for i in range(1,11):
       print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("invalid input")

print("we are done")
print("bye")