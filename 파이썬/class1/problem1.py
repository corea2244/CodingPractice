# 11720번 : 숫자의 합
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

count = int(input())
number = input()
sum = 0

for i in range(count):
    sum = sum + int(number[i])

print(sum)