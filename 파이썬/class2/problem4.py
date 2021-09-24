# 15829번 : Hashing


strlen = int(input())
str = input()
sum = 0
for i in range(strlen):
    j = ord(str[i])-96
    sum += j*pow(31,i)

print(sum%1234567891)