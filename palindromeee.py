def is_palindrome(s):
    return s == s[::-1]

s = "1001"
ans = is_palindrome(s)

if ans:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
    