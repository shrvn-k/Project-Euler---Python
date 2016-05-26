def count_factors(n):
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

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