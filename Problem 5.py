"""i=1
check=[11,13,14,16,17,18,19,20]
while True:
    count=0
    for x in check:
        if i%x==0:
            count+=1
    if count==20:
        print i
        break
    i+=2520

"""

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

solution = find_solution(20)
if solution is None:
    print "No answer found"
else:
    print "found an answer:", solution
