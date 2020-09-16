#Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on...
t=int(input())
l=[]
p=[]
for i in range(t):
    n=int(input())
    l=[int(x) for x in input().split(' ')]
    i=0
    j=n-1
    m=[]
    for k in range(n):
        if(k%2==0):
            m.append(l[j])
            j=j-1
        else:
            m.append(l[i])
            i=i+1
    p.append(m)
for i in range(t):
    for item in p[i]:
        print(item,end=' ')
    print()
            
    
