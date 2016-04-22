def is_palindrome(n):
    n1=n
    p=""
    for i in n:
        p=i+p
    if n1==p:
        return True
    return False

print is_palindrome("123")
print is_palindrome("121")
print is_palindrome("585")
print is_palindrome(bin(585))
