import time
anim1 = "⬛"
anim2 = "⬜"
anim2N=6
animN=74
def progbar1():
    i=0
    j=0    
    h=animN
    while True:       
        print(anim1*j+anim2*h,end='\r')
        
        time.sleep(.1)
        if i<animN:
            j+=1
            h-=1  
        else:     
            j-=1
            h+=1   
        i+=1
        if(i==animN*2):
            break
def progbar2():
    i=0
    j=0    
    k=0
    h=animN
    while True:               
        print(anim2*k+anim1*j+anim2*h,end='\r')        
        time.sleep(.1)
        if k==j==h==0:
            break
        if j>anim2N:
            k+=1
            j=anim2N-1            
        j+=1
        h-=1
        i+=1
        if i==(animN*2-8):
            k=0
            j=0
            h=0

def progbar3():
    an = [
        "/",
        "―",
        "\\",
        "|"
    ]
    i=0
    while True:               
        print("Загрузка:"+"    "+an[i%len(an)]+"    ",end='\r')        
        time.sleep(.2)
        i+=1
        if(i==animN//4):
            break