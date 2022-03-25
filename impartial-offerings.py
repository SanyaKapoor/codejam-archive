t = int(input())
for i in range(t):
    n = int(input())
    a = [int(s) for s in input().split(" ")]
    a.sort()
    treat = 1
    treats = 1
    for j in range(n-1):
        if a[j+1]>a[j]:
            treat = treat + 1
        treats = treats + treat
    print("Case #"+str(i+1)+": "+str(treats))