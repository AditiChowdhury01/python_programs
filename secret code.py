st = input("enter the message")
words = st.split(" ")
coding = True
if (coding):
  nwords = []      
  for word in words:
    if (len(word)>=3):
     r1  = "thy"
     r2 = "rde"
     stnew = r1 + word[1:] + word[0] + r2
     nwords.append(stnew)

    else:
     nwords.append(st[::-1])
  print(" ".join (words))
  
else:
  for word in words:
   if (len(st)>=3):
   
    print(st[-1] + st[:-1] )
  else:
    print(st[::-1])
print(" ".join (words))
  