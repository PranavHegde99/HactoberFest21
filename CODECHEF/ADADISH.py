tc = int(input())
while tc !=0:
    n= int(input())
    dish = list(map(int, input().split()))
    if n==1:
        print(dish[0])
    else:
        dish.sort(reverse=True)
        time=dish[1]
        dish.append(45)
        temp=abs(dish[0]-dish[1])
        for i in range(2,n+1):
            time = time + min(temp,dish[i])
            temp = abs(temp-dish[i])
        print(time)
        
    tc -= 1
