#Some prime numbers can be expressed as a sum of other consecutive prime numbers
#Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
import math
def isprime(n):
    flag=0
    for i in range(2,math.ceil(n/2)+1):
        if(n%i==0):
            flag=1
            break
    return flag
l=[]
n=int(input())
c=0
for i in range(2,n+1):
    q=isprime(i)
    if(q==0):
        l.append(i)
sum=2
for i in range(1,len(l)):
        sum=sum+l[i]
        if(sum in l):
            c=c+1
        if sum>n:
            break
print(c)    
        