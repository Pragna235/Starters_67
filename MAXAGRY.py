# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    s=(n*(n-1))//2
    #print("first s = ",s)
    if(k<n//2):
        #print("k = ",k)
        x=n-2*k 
        #print("x = ",x)
        s-=(x*(x-1))//2
        #print("second s = ",s)
    print(s)