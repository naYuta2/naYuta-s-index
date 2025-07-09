N, W = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        if j == A[i-1]:
            dp[i][j] = True
            continue

        if i-1>0:
            if dp[i-1][j]:
                dp[i][j] = True
                continue
            if j-A[i-1]>0:
                if dp[i-1][j-A[i-1]]:
                    dp[i][j] = True
ans = 0
for i in range(1, W+1):
    if dp[-1][i]:
        ans += 1

print(ans)