# 2609번 : 최대공약수와 최소공배수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

a, b = list(map(int,input().split(' ')))
first = 0
second = 0
for i in range(a):
    if a%(a-i)==0 and b%(a-i)==0:
        first = a - i
        break

count = 0
while True:
    count += 1
    if (a * count)%b==0:
        second = a * count
        break

print(first)
print(second)