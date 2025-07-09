N = int(input())
d = list(map(int, input().split()))
t = list(map(int, input().split()))

arr = [(t[i], d[i]) for i in range(N)]
arr.sort()

time = 0
flag = True
for i in range(N):
    time += arr[i][1] # arr[i][1] : i番目の仕事をこなすのにかかる時間
    if time > arr[i][0]: # arr[i][0] : i番目の仕事の締め切り
        flag = False
        break

print("Yes" if flag else "No")