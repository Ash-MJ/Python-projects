
#given an unsorted array A of size N of non negative integers, 
#find a continuous sub array which adds to a given number S
t=int(input())
n=[]
s=[]
k=[]
for i in range(t):
    a,b=[int(x) for x in input().split(" ")]
    n.append(a)
    s.append(b)
    m=[int(x) for x in input().split(' ')]
    k.append(m)
for i in range(t):
    print()
    for j in range(n[i]-1):
        if(sum==s[i]):
            break
        sum=0
        for q in range(j,n[i]):
            
            if(sum<s[i]):
                sum=sum+k[i][q]
            elif(sum==s[i]):
                print(j+1,' ',q)
                print()
                break
            else:
            
                break
    
            

   
    
    
    
