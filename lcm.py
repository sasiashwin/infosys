def lcm(x,y):
    if(x>y):
        lcm = x
    else:
        lcm = y
    while(lcm):
        if(lcm%x==0 and lcm%y==0):
            break
        lcm+=1
    return lcm
x=22
y=26
print(lcm(x,y))
