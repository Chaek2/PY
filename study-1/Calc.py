col = int(input("Количество: "))
n1 = float(input("Число: "))
n2 = float(input("Число: "))
z = input("Знак (+,-,//,/,%,*,^): ")
i=1

def Actd(n1,n2):
    match z:
        case '+':
            n3 = n1 + n2            
            print(n1,z,n2,"=",n3)                                   
            n1 = n3                            
        case '-':
            n3 = n1 - n2
            print(n1,z,n2,"=",n3)   
            n1 = n3              
        case '%':               
            n3 = n1 % n2
            print(n1,z,n2,"=",n3)   
            n1 = n3              
        case '/':            
            n3 = n1 / n2
            print(n1,z,n2,"=",n3)   
            n1 = n3                        
        case '^':
            n3 = n1 ** n2
            print(n1,z,n2,"=",n3)   
            n1 = n3
        case '//':            
            n3 = n1 // n2
            print(n1,z,n2,"=",n3)   
            n1 = n3            
        case '*':
            n3 = n1 * n2
            print(n1,z,n2,"=",n3)   
            n1 = n3      
    return n1
    
if(col > 0):                           
    if(col == 1):                        
        while (i<col+1):                                   
            i+=1             
            if((z == '//' or z == '/' or z == '%')and n2!=0):
                n1 = Actd(n1,n2)                                        
            elif(z == '+' or z == '-' or z == '*' or z == '^'):
                n1 = Actd(n1,n2)                                     
            else:
                i-=1  
                n1 = float(input("Число: "))
                n2 = float(input("Число: "))
                z = input("Знак (+,-,//,/,%,*,^): ")                 
    elif(col > 1):
        if((z == '//' or z == '/' or z == '%')and n2!=0):
            n1 = Actd(n1,n2)                            
        elif(z == '+' or z == '-' or z == '*' or z == '^'):
            n1 = Actd(n1,n2)     
        else:
            i-=1
        while (i<col):
            i+=1
            n2 = float(input("Число: "))
            z = input("Знак: ")    
            if((z == '//' or z == '/' or z == '%')and n2!=0):
                n1 = Actd(n1,n2)                            
            elif(z == '+' or z == '-' or z == '*' or z == '^'):
                n1 = Actd(n1,n2)     
            else:
                i-=1          
