b=0
YY=-1
def MM(r): 
    a = 0   
    for i in range(1,r+1):        
        a+=i%10+i//10              
    return a
while(YY<0):
    YY = int(input("Год: "))
b+= MM(31)*7
if(YY%4==0 and (YY//100)%4==0):
    b+= MM(29)
else:
    b+= MM(28)
b+= MM(30)*4
print("YY: "+str(b))
