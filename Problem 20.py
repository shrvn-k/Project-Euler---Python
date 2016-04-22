import math
n=math.factorial(100)
sum=0
while n!=0:
    r=n%10
    sum+=r
    n=n/10
print sum
