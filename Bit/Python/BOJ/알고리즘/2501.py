# 24.02.29 - yuna,oh
# easy

n, k = map(int, input().split())

cnt = 0
res = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            res = i
            break

print(res)

