#There is a range given n and m in which we have to find the count all the prime pairs whose difference is 6. We have to find how many sets are there within a given range.

def isprime(k):
    for i in range(2,int(k/2)):
        if(k%i==0):
            return 0
    return 1
a,b=[int(x) for x in input().split(" ")]
l=[]
c=0
for i in range(a,b):
    if(isprime(i)):
        l.append(i)
for item in l:
    if item+6 in l:
        c=c+1
print(c)
    