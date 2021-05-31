def fibonnaci(n):
    a = 0
    b = 1 
    s = 0
    cnt = 1 
    while(cnt<=n):
        print(s,end=" ")
        a = b
        b = s 
        s = a+b
        cnt +=1 
fibonnaci(5)

def fibonnaci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1 
    else:
        return fibonnaci(n-2)+fibonnaci(n-1)
n=5
for i in range(1,n+1):
    print(fibonnaci(i),end=" ")
