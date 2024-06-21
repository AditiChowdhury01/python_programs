# def list_sum(numlist):                    //sum of all list items
#     if(len(numlist))==1:
#         return numlist[0]
#     else:
#         return numlist[0]+list_sum(numlist[1:])
# print(list_sum([2,3,4,5]))


# def fact(n):             //factorial
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# def fibo(n):                                   //fibonacci sequence
#      if (n ==1 or n==2):
#           return 1
#      else:
#           return fibo(n-1) + fibo(n-2)
# print(fibo(4))


# def sum(n):                                     //sum of digits
#     if n==0:
#         return 0
#     else:
#         return n%10 +sum(int(n/10))
# print(sum(345))


# def sum_dig(n):                       //sum of digits upto n==0
#     if n == 0:
#         return 0
#     else:
#         return n + sum_dig(n-2)
# print(sum_dig(6))


# def h_mean(n):                       //harmonic mean
#     if n==1:
#         return 1
#     else:
#         return 1/(n) + h_mean(n-1)
    
# print(h_mean(4))


# def gsum(n):                  //geometric sum
#     if n<0:
#         return 0
#     else:
#         return 1/(pow(2,n)) + gsum(n-1)
# print(gsum(4))


# def  pow(a,b):                //a**b
#     if b==0:
#         return 1
#     else:
#         return a *pow(a,b-1)
# print(pow (2,3))


# def gcd(a,b):                     //gcd
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(4,6))