def check_palindrome(word):
    # Compare the word with its reverse
    return word == word[::-1]

# Test case
status = check_palindrome("malayalam")

if status:
    print("word is palindrome")
else:
    print("word is not palindrome")
