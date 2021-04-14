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


def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
n=5
for i in range(0,n):
    print(fibonacci(i),end=" ")
