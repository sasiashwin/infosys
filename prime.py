def prime(num1,num2):
    for i in range(num1,num2+1):
        cnt = 0
        for j in range(2,i//2+1):
            if(i%j==0):
                cnt+=1 
        if(cnt==0):
            print(i,end=" ")
prime(900,1000)    
            
