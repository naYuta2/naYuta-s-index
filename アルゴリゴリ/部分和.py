def func(i, j):
    # i: 先頭からi個使って
    # j: 合計jを作れるか
    if memo[i][j] != None: return memo[i][j]

    if i == 0:
        # 全ての数字を使って合計がWになったらTrue
        memo[i][j] = True if j == 0 else False
    else:
        memo[i][j] = False
        # arr[i-1]を使う場合
        if j>=arr[i-1] and func(i-1, j-arr[i-1]):
            memo[i][j] = True
        # arr[i-1]を使わない場合
        if func(i-1, j):
            memo[i][j] = True
    
    return memo[i][j]

N, W = map(int, input().split())
arr = list(map(int, input().split()))
memo = [[-1] * (W+1) for _ in range(N+1)]
# -1: 未記録, 0: false, 1: true

print("Yes" if func(N, W) else "No")