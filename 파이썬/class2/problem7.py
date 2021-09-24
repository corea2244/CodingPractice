# 11050번 : 이항 계수 1

a, b = list(map(int, input().split(' ')))
upside = 1
downside = 1
for i in range(b):
    upside *= (a-i)
for i in range(b):
    downside *= (b-i)

print(upside//downside)