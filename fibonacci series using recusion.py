# Fibonacci
# F(0) = 0
# F(1) = 1
# n > 1: F(n) = F(n-1) + F(n-2)

# Time: O(2^n), Space: O(n)

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return f(n-1) + f(n-2)
    
print(f(5))
