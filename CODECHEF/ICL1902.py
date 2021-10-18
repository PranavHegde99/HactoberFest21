import numpy as np
tc = int(input())
while tc!=0:
    n = int(input())
    count=0
    while n!=0:
        n = n - np.square(int(np.sqrt(n)))
        count = count + 1
    print(count)
    tc -= 1
