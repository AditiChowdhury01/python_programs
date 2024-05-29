import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
hour = int(input("enter hour: "))
print(hour)

if(hour<=00 and hour==12):
    print("good morning")
elif(hour>12 and hour<=16):
    print("good afternoon")
elif(hour>16 and hour==19):
    print("good evening")
else:
    print("good night")