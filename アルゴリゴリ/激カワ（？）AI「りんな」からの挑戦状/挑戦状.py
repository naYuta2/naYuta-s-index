import copy

def func(idx, length, frag):
    max_length = length
    saigo = s[idx][-1]
    for i in range(N):
        if frag[i]:
            continue
        if saigo == s[i][0]:
            frag[idx] = True
            next_length = func(i, length+1, frag)
            max_length = max(next_length, max_length)
            frag[i] = False
    return max_length

N = int(input())
s = list(list(map(str, input().split())))

frag = [False] * N

ans = 0
for i in range(N):
    p = func(i, 1, copy.copy(frag))
    ans = max(p, ans)
print(ans)