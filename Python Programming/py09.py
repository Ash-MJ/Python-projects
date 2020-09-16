#Bastin once had trouble finding the numbers in a string. The numbers are distributed in a string across various test cases. There are various numbers in each test case you need to find the number in each test case. Each test case has various numbers in sequence. You need to find only those numbers which do not contain 9. For eg, if the string contains "hello this is alpha 5051 and 9475".You will extract 5051 and not 9475. You need only those numbers which are consecutive and you need to help him find the numbers. Print the largest number.

#Note: Use long long for storing the numbers from the string.
t=int(input())
for i in range(t):
    p=[]
    a=input()
    l=list(a.split(" "))
    for item in l:
        if(item.isnumeric()):
            k=list(item)
            if('9' in k):
                continue
            else:
                p.append(item)
if(len(p)==0):
    print(-1)
else:
    print(max(p))