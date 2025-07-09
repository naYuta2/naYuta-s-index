n = int(input())
memo = [-1] * n
fibo = [0, 1]

def culc_fibo(n):
    if memo[n] != -1:
        return memo[n]
    
    if n < len(fibo):
        memo[n] = fibo[n]
        return memo[n]
    return culc_fibo(n-1) + culc_fibo(n-2)

print(culc_fibo(n-1))