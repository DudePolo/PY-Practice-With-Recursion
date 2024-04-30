# Write code for algorithm 3 below
def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
result = fibonacci(7)
print("The 7th element in the Fibonacci sequence is:", result)