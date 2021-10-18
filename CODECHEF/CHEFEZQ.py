tc = int(input())
while tc !=0:
    n,k= map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    count = 0
    while True:
        if i+1==n:
            while True:
                if arr[i]<=k:
                    print(i+1)
                    count = 1
                    break
                else:
                    print(i+arr[i]//k+1)
                    count = 1
                    break
        if count == 1:
            break
        if arr[i]<k:
            print(i+1)
            break
        else:
            temp = arr[i]-k
            arr[i+1] += temp
            i+=1
        
    tc -= 1
