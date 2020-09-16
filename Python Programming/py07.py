#Given two arrays X and Y of positive integers, find number of pairs such that xy > yx (raised to power of) where x is an element from X and y is an element from Y.
t=int(input())
p=[]
for i in range(t):
    m,n=[int(x) for x in input().split(' ')]
    x=[int(k) for k in input().split(' ')]
    y=[int(k) for k in input().split(' ')]
    c=0
    for i in range(m):
        for j in range(n):
            if(x[i]**y[j]>y[j]**x[i]):
                c=c+1
    p.append(c)
for item in p:
    print(item,end=' ')