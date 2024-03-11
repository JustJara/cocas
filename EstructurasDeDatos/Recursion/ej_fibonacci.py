def badfibonacci(n):
    #Retorna el número Fibonacci número N

    if (n<=1):
        return n
    else:
        return badfibonacci(n-2) + badfibonacci(n-1)

print(badfibonacci(8))

def good_fibonacci(n):
    print(f"calculo fibonacci {n}")
    if n<=1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b, a)

print(good_fibonacci(8))