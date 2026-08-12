<<<<<<< HEAD
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        return True
    else:
        return False

n = int(input("enter a number: "))
# Fixed the spelling typo below (added the missing 'n')
if is_palindrome(n): 
    print("the number is a palindrome.")
else:
    print("the number is not a palindrome.")
=======
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        return True
    else:
        return False

n = int(input("enter a number: "))
# Fixed the spelling typo below (added the missing 'n')
if is_palindrome(n): 
    print("the number is a palindrome.")
else:
    print("the number is not a palindrome.")
>>>>>>> 74749572667462e54cbe4527c6342a979a9c1499
