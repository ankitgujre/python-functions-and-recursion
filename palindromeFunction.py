def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

# Input
text = input("Enter a string: ")

# Function Call
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
