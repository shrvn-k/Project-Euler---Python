"""def triangular_no(n):
    num=0
    for x in range(0,n+1):
        num+=x
    return num
"""
def count_factors(n):
    count=0
    for x in range(1,n+1):
        if n%x==0:
            count+=1
    return count

def prob_12():
    count=0
    i=0
    while count<500:
        i+=1
        x=(i*(i+1))/2
        count=count_factors(x)
        if i%100==0:
            print i,x,count
    print "ans=",x,count

prob_12()

