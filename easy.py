#easy (from last)

#1

c=0
while(True):
    a=int(input())
    if a=="42":
        break
    else:
        print(a)

#2

import random
x,y=input().split()
x=int(x)
y=int(y)
c=str(x-y)
d=random.uniform(1,9)
c[0]=str(d)
print(c)


#challenge

#1

a=int(input())
for i in range(a):
    d,x,y,z=map(int,input().split())
    l=[]
    b=x*7
    l.append(b)
    c=y*d+z*(7-d)
    l.append(c)
    print(max(l))

#2

a=int(input())
for i in range(a):
    x,y=map(int,input().split())
    c=(y*y)/(2*x)
    print("%.0f"%c)


#factorial 

a=int(input())
for i in range(a):
    x=int(input())
    b=len(str(x))
    s=0
    for i in range(1,b+5):
        if x/(5**i) >=1:
            s=s+int(x/(5**i))
    print(s)

#############33    sample of finding trialing zereos  ################

a=int(input())
s=0
for i in range(1,11):
    if a/(5**i) >=1:
        s=s+int(a/(5**i))
print(s)
#########################################################################

#4

import random
x,y=map(int,input().split())
a=x-y
b=str(a)
c=b[:1]
d=b[1:]
l=['1','2','3','4','5','6','7','8','9']
l.remove(c)
print(str(random.choice(l))+str(d))

############################### approach 1 (not submitted)          #########

a=int(input())
for i in range(a):
    x=int(input())
    l = list(map(int, input().strip().split(' ')[:x]))
    l.sort()
    a=min(l)
    l.remove(a)
    b=min(l)
    l.remove(b)
    print(b-a)

###################################################

#5

a=int(input())
for i in range(a):
    x=int(input())
    l = list(map(int, input().strip().split(' ')[:x]))
    l.sort()
    diff=max(l)
    for i in range(len(l)-1):
        if l[i+1]-l[i]<diff:
            diff=l[i+1]-l[i]
    print(diff)

#6

a=int(input())
for i in range(a):
    x=int(input())
    l = list(map(int, input().strip().split(' ')[:x]))
    k=int(input())
    c=l[k-1]
    l.sort()
    print((l.index(c))+1)

#7

a=int(input())
for i in range(a):
    x,y,k,n=map(int,input().split())
    ok=0
    for i in range(n):
        p,c=map(int,input().split())
        if p>=x-y and k>=c:
            ok=ok+1
    if ok>0:
        print("LuckyChef")
    else:
        print("UnluckyChef")

#8

a=int(input())
for i in range(a):
    c=0
    j=input()
    s=input()
    for i in s:
        if i in j:
            c+=1
    print(c)

#9

a=int(input())
for i in range(a):
    x=input()
    if "101"  in x or "010" in x:
        print("Good")
    else:
        print("Bad")

#10

a=int(input())
for i in range(a):
    n,k=map(int,input().split())
    if k==0:
        print(0,n)
    else:
        print(n//k,n%k)

#11

a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=0
    for j in range(b,c+1):
        if j%10==2 or j%10==3 or j%10==9:
            d+=1
    print(d)