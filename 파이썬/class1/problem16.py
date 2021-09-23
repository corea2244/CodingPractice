# 10818번 : 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

num = input()
arr = list(map(int,input().split()))
print(min(arr),end=' ')
print(max(arr))