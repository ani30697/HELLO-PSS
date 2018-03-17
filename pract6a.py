def reverse(s):
    return s[::-1]

def ispalindrome(s):
    rev=reverse(s)
    if (s==rev):
      return True
    return False
s='malayalam'
print(reverse(s))
print(ispalindrome(s))
ans=ispalindrome(s)
if ans==1:
    print("it is a palindrome")
else:
    print("it is not")
