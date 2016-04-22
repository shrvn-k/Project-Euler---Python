def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

lst=[x for x in range(2,2000000) if x%2!=0]
lst=[x for x in lst if x%3!=0]
lst=[x for x in lst if x%5!=0]
lst=[x for x in lst if x%7!=0]
lst=[x for x in lst if x%11!=0]
def sum_of_primes():
    sum=25
    for i in lst:
        if is_prime(i):
            sum+=i
            print i,sum
    print sum

sum_of_primes()
