tc = int(input())
while tc !=0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min = 1000000001    
    for i in range(n-1):
        if abs(arr[i]-arr[i+1])<min:
                min = abs(arr[i]-arr[i+1])
    print(min)
    tc -= 1
