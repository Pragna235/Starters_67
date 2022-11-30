# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c1,c2=0,0
    
    for i in range(n):
        if(arr[i]%2==0):
            c2+=1
        else:
            c1+=1
    if(c1%2==0 and c1!=0):
        print("YES")
    else:
        print("NO")
        