#problem 6
def soln(n):
    sos= ((n**3)/3)+((n**2)/2)+(n/6)+1
    sosn=(n*(n+1))/2
    print (sosn**2)-sos
soln(100)
