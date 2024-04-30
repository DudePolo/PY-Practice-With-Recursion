# Write code for algorithm 5 below
def is_palindrome(s):
    # Convert the string to lowercase to ignore case sensitivity
    s = s.lower()
    # Remove any non-alphanumeric characters from the string
    s = ''.join(char for char in s if char.isalnum())
    # Compare the original string with its reverse
    return s == s[::-1]

# Example usage:
result1 = is_palindrome("radar")
print("Is 'radar' a palindrome?", result1)

result2 = is_palindrome("hello")
print("Is 'hello' a palindrome?", result2)
