import BD, Main, os,animation
import time as t

def registr():    
    log = input("Введите номер телефона (79123456789): ")
    pas = input("Введите пароль (Aqr90_): ")
    BD.Row("Player",[log,pas],"I")
    animation.progbar3()
    t.sleep(2)
    BD.AddMoney(log)
    Main.menu(log)

def autorisathion():    
    log = input("Введите номер телефона: ")
    pas = input("Введите пароль: ")
    rec = BD.Row("Player",(log),"S")
    animation.progbar3()
    os.system('cls')  
    if not rec:
        print("Нет таких данных")        
        t.sleep(2)
        os.system('cls')        
        autorisathion()
    else:
        for row in rec:
            if pas == row[2]:
                Main.menu(log)
            else:
                os.system('cls')
                print("Не правильный пароль")                
                t.sleep(2)
                os.system('cls')
                autorisathion()       