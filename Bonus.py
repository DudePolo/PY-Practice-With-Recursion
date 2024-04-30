def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
result = gcd(24, 36)
print("The greatest common divisor of 24 and 36 is:", result)