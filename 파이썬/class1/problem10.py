# 2438번 : 별 찍기 - 1
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

num = int(input())
for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print()

