arr = list(map(int, input().split()))
K = int(input())

dp = [1] * len(arr)
for i in range(len(arr)):
    '''私が書いたクソコード
    n = arr[i]
    length = 1
    for j in range(i, K):
        if arr[j] - n <= K:
            n = arr[j]
            length += 1
    ans = max(ans, length)
    '''
    # 以降AI様のコメントを基に作成したコード
    kouho = []
    for j in range(i):
        if arr[j] < arr[i]:
            if arr[i] - arr[j]  <= K:
                dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))