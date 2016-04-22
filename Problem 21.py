def sum_of_factors(n):
    count=0
    sum_fact=0
    for x in range(1,n):
        if n%x==0:
            sum_fact+=x
    return sum_fact

i=1
lst=[]
while i<10000:
    a=sum_of_factors(i)
    b=sum_of_factors(a)
    if i==b and i!=a:
        print i
        lst.append(i)
    i+=1
print "sum=",sum(lst)
