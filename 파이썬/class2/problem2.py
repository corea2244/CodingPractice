# 4153번 : 직각삼각형
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

while True:
    arr = list(map(int,input().split(' ')))
    if arr[0]==0 and arr[1]==0 and arr[2]==0:
        break
    minNum = arr.pop(arr.index(min(arr)))
    middleNum = arr.pop(arr.index(min(arr)))
    maxNum = arr.pop(arr.index(min(arr)))
    if pow(minNum,2)+pow(middleNum,2) == pow(maxNum,2):
        print("right")
    else:
        print("wrong")