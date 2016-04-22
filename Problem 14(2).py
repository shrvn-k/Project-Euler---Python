i=1
lst=[]
maximum=maxn=0
while i<1000000:
    n=i
    lst.append(n)
    while n!=1:
        if n%2==0:
            n=n/2
            lst.append(n)
        else:
            n=(3*n)+1
            lst.append(n)
    print i,len(lst)
    if len(lst)>maximum:
        maximum=len(lst)
        maxn=i
    lst=[]
    i+=1
print maximum,maxn
