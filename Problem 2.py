sum=0
a=1
b=0
n=0
while n<4000000:
    n=a+b
    a=b
    b=n
    if n%2==0:
        sum+=n
print sum
