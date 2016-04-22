max=0
def is_palindrome(n):
    n1=n
    num=0
    while(n!=0):
        r=n%10
        num=(num*10)+r
        n=n/10
    if num==n1:
        return True
    else:
        return False
"""
while(a>500 and b<500):
    if is_palindrome(a*b):
        if a*b>max:
            max=a*b
            print max
    else:
        b+=1
        
print max
"""

for x in range(1,1000):
    for y in range(1,1000):
        if is_palindrome(x*y):
            if x*y>max:
                max=x*y
                print max
print max
