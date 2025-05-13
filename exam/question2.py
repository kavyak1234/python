def is_palindrome(a):
    a=a.lower()
    return a==a[::-1]
print(is_palindrome,"hello")