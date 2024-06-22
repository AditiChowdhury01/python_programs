# def average ( a , b):
#     sum = (a + b )/2
#     print(sum)

# average( 6 , 8)

def average(*numbers):
    sum = 0
    for i in numbers:
     sum = sum +i
    print("the average is" ,sum/len(numbers))

average(3 , 4 )

def name(**name):
   print("hello," , name["fname"] ,name["mname"] , name["lname"])
   
name(fname = "aditi", mname = "rao" , lname = "hydari")