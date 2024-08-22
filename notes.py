def is_palindrome(s):
  if len(s) <= 1:
    return True

  if s[0] != s[-1]:
    return False

  return is_palindrome(s[1:-1])


print(is_palindrome("racecar"))
print(is_palindrome("tool"))
print(is_palindrome("abba"))


elements = [1, 3, 8, 11, 12, 15]

# linear search n      Worst Case: O(n)
# binary search n      Worst Case: O(log(n))

if 12 in elements
