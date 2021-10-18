tc = int(input())
while tc !=0:
    arr = list(map(int, input().split()))
    i = arr[2]
    while True:
        if i==arr[3]:
            print('YES')
            count = 1
            break
        i = (i+arr[1])%arr[0]
        count = 0
        if i==arr[2]:
            break      
    if count == 0:
        print('NO')      
    tc -= 1
