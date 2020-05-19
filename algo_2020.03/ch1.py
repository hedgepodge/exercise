def is_palindrome(word):
    if word == word[::-1]:
        return("True")
    else:
        return("False")

# test
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
