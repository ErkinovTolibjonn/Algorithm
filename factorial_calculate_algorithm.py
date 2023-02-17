def factorial(n):
    count = 1
    for i in range(1,n+1):
        count *= i
    return count
func = factorial(5)
print(func)