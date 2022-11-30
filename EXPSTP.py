# cook your dish here
for t in range(int(input())):
    n,x1,y1,x2,y2=map(int,input().split())
    
    a=min(min(n-x1+1,n-y1+1),min(x1,y1))
    b=min(min(n-x2+1,n-y2+1),min(x2,y2))
    c=abs(x1-x2)+abs(y1-y2)
    
    if(x1<1 and y1>n and x2<1 and y2>n):
        print(0)
    elif(x1<1 or y1>n):
        print(min(min(n-x2+1,n-y2+1),min(x2,y2)))
    elif(x2<1 or y2>n):
        print(min(min(n-x1+1,n-y1+1),min(x1,y1)))
    else:
        print(min(c,a+b))
    
    
    
    
        
        