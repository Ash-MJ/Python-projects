# Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to.
#He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box.
#Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. Assume that there are an infinite number of empty boxes available.
#At a time he can pick up any two boxes for transferring and if both the boxes contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. As he is too eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected
t=int(input())
s=[]
for i in range(t):
    sum=0
    n=int(input())
    l=[int(x) for x in input().split(' ')]
    while(len(l)>=2):
        a=l.pop(0)
        b=l.pop(0)
        k=a+b
        sum=sum+k
        l.insert(0,k)
    s.append(sum)
print(s)
        
    
    
    