def fibo(n):

    if not n:
        return [0]
    if n == 1:
        return [0, 1]
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci


print(fibo(8))