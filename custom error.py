a = int(input("enter a number between 5 and 9 : "))

if(a == "quit"):
    print("ok no error")
    
elif(a<5 or a>9):
    raise ValueError("some error with the number")