#problem 9
"""
for a in range(0,1000):
    for b in range(0,1000-a):
        for c in range(0,1000-b):
            print a,b,c
            if a+b+c==1000 and (a*a)+(b*b)==(c*c):
                print a*b*c
                break
        
"""
"""
a=[x**2 for x in range(0,1000) if x<1000]
b=[x**2 for x in range(0,1000) if x<1000]
c=[x**2 for x in range(0,1000) if x<1000]
for i in a:
    for j in b:
        for k in c:
            if (i**0.5)+(j**0.5)+(k**0.5)==1000.0:
                print (i**0.5),(j**0.5),(k**0.5)
                if i+j==k:
                    print "ans="
                    print (i**0.5)*(j**0.5)*(k**0.5)
                    break
print "end"
"""

for x in range(0,1000):
    for y in range(0,1000):
        z=1000-x-y
        if (x*x)+(y*y)==(z*z):
            print x*y*z
