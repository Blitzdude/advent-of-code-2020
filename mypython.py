
print("Hello World!")

# fibonacci sequense
def fib(n):
    """Print a Fibonacci sereis up to n."""
    a = 0
    b = 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
        
    print()

fib(2000)