tc = int(input())
while tc !=0:   
    r,z = map(int, input().split())
    a = r//10 
    b = r%10
    c = z//10
    d = z%10
    i=0
    j=0
    k=0
    l=0
    if a==0 and c==0:
        print(r+z)
    else:
        if a==0 and c!=0:
            k = (a*10+c)+(b*10+d)
            l = (a*10+d)+(c*10+b)
        if a!=0 and c==0:
            i = (c*10+b)+(a*10+d) 
            j = (d*10+b)+(c*10+a)
        if a!=0 and c!=0:
            k = (a*10+c)+(b*10+d)
            l = (a*10+d)+(c*10+b)
            i = (c*10+b)+(a*10+d) 
            j = (d*10+b)+(c*10+a)
        print(max(i,j,k,l,r+z))
    tc -= 1
