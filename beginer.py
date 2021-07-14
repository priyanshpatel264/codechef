# 1

x,y=input().split()
x=int(x)
y=float(y)
if x%5==0 and x+0.5<=y:
    c=y-x-0.50
    print("%.2f"%c)
else:
    print("%.2f"%y)


# 2
n,k=input().split()
n=int(n)
k=int(k)
a=[]
for i in range(n):
    x=int(input())
    if x%k==0:
        a.append(x)
print(len(a))

# 3

a=int(input())
for i in range(a):
    x,y=input().split()
    x=int(x)
    y=int(y)
    print(x+y)

# 4

a=int(input())
print(a)

# 5

a=int(input())
for i in range(a):
    x=int(input())
    sum=0
    while(x>0):
        c=x%10
        sum=sum+c
        x=x//10
    print(sum)

# 6

a=int(input())
for i in range(a):
    x,y=input().split()
    x=int(x)
    y=int(y)
    print(x%y)

# 7

a=int(input())
for i in range(a):
    x=input()
    sum=int(x[0])+int(x[len(x)-1])
    print(sum)

# 8

a=int(input())
for i in range(a):
    x=int(input())
    sum=1
    while(x>0):
        sum=sum*x
        x=x-1
    print(sum)

# 9

a=int(input())
b=[]
for i in range(a):
    x=int(input())
    b.append(x)
c=sorted(b)
for i in range(a):
    print(c[i])

# 10

a = int(input())
for i in range(a):
    print(input().count('4'))

# 11

a=int(input())
for i in range(a):
    x=input()
    print(x[::-1])

# 12

import math
a=int(input())
for i in range(a):
    x=int(input())
    print(int(math.sqrt(x)))

# 14

a=int(input())
b=[]
for i in range(a):
    x,y,z=input().split()
    x=int(x)
    y=int(y)
    z=int(z)
    b.append(x)
    b.append(y)
    b.append(z)
    b.sort(reverse=True)
    print(b[1])
    b=[]

# 15

a=int(input())
for i in range(a):
    x=int(input())
    sum=1
    while(x>0):
        sum=sum*x
        x=x-1
    print(sum)

# 16

a=int(input())
for i in range(a):
    x=int(input())
    if x<10:
        print("Thanks for helping Chef!")
    else:
        print("-1")
