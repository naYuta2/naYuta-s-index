N, M = map(int, input().split())
a = list(map(int, input().split()))

arr = []
for i in range(N):
    for j in range(N):
        arr.append(a[i] + a[j])

arr.sort()

ans = 0
frag = False
for i in range(len(arr)):
    p1 = arr[i]
    p2 = -1
    m = M - p1
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] <= m:
            p2 = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    if p2 != -1:
        ans = max(ans, p1 + p2)
        if ans == M:
            break

print(ans)