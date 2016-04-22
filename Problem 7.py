def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True


def nth_prime_no(n):
    count=1
    i=2
    while count<=n:
        if is_prime(i):
            print count,i
            count+=1
            i+=1
        else:
            i+=1

print nth_prime_no(10001)
