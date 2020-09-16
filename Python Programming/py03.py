t=int(input())
s=[]
for i in range(t):
    sum=0
    n=int(input())
    l=[int(x) for x in input().split(' ')]
    l=l.sort()
    if(len(l)!=0): 
        a=l.pop(0)
        b=l.pop(0)
        k=a+b
        sum=sum+k
        l.insert(0,k)
    s.append(sum)
print(s)
        
    
    
    