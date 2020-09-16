#Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).
t=int(input())
l=[]
for i in range(t):
    x,y=[int(k) for k in input().split(' ')]
    m=[]
    p=[int(k) for k in input().split(' ')]
    q=[int(k) for k in input().split(' ')]
    r=0
    s=0
    while(r<x or s<y):
        if(r==x and s<y):
            while(s<y):
                m.append(q[s])
                s=s+1
            break
        elif(s==y and r<x):
            while(r<x):
                m.append(p[r])
                r=r+1
            
        if(p[r]<q[s]):
            m.append(p[r])
            r=r+1
        else:
            m.append(q[s])
            s=s+1
    l.append(m)
for i in range(t):
    for item in l[i]:
        print(item,end=' ')
    print()
    

        
    
    
    


