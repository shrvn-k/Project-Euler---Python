lst=[]
print "start"
for a in range(2,101):
    for b in range(2,101):
        if a**b not in lst:
            lst.append(a**b)
print len(lst)
