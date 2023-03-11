import BD,Main,pick,os, random
import keyboard,Cheque
import time as t
selected = 1
global rec,rows,log

def BuyComponent(_log):
    global rec,rows,log
    log=_log
    titles = 'Еда: '
    options=[]
    for row in BD.Row("Dish",options,"S"):
        options.append(row[1])
    option, index = pick.pick(options, titles, indicator='=>')
    rows = BD.Row("Component",(option),"S")
    rec = list(BD.Row("Component",[],"S"))
    i=0
    for ij in rec:     
        try:   
            rec[i]=list(rec[i])
            tec = rec[i]
            tec[2]=0
            j=0
            for jj in rows:
                lec = list(rows[j])
                lec = rows[j]
                if lec[0] == tec[0]:
                    tec[2]=lec[2]
                j+=1
            i+=1
        except:
            titles = 'Еда: '
    Component()

def Component():
    os.system('cls')
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('right', right)
    keyboard.add_hotkey('left', left)
    keyboard.add_hotkey('enter', enter)
    keyboard.wait()

def show_menu():
    global selected,rec
    os.system('cls')
    print("Ингридиенты:")
    print("Кошелёк: "+str(Balance()))
    print()
    for i in range(len(rec)):
        print("{0} {2} {3} {1}".format(">" if selected == i else " ", "<" if selected == i else " ",rec[i][1],rec[i][2]))
    print()
    print("Цена: "+str(Sam()))


def up():
    global selected
    if selected == 0:
        return
    selected -= 1
    show_menu()

def down():
    global selected,rec
    if selected == len(rec)-1:
        return
    selected += 1
    show_menu()

def right():
    global rec,selected   
    rec[selected]=list(rec[selected])
    tec = rec[selected]
    if(tec[2]<tec[4]):
        tec[2]+=1
    show_menu()

def left():
    global rec,selected      
    rec[selected]=list(rec[selected])
    tec = rec[selected]
    if(tec[2]>0):
        tec[2]-=1
    show_menu()

def enter():
    global rec,log      
    sam =Sam()
    bal=Balance()
    if(bal>=sam):
        full=0
        ran = random.randint(0,100)
        if(ran == 3):
            full=bal/100*30
            print("Попался глаз. Скидка 30%")
            t.sleep(2)
        bal-=(sam-full)        
        balance = BD.UpdateBalance(log,bal,sam)
        BD.UpdateSkald(rec)
        Cheque.cheque(rec,balance)
        Main.menu(log)
    else:
        print()
        print("Недостаточно денег: "+str(Sam()-Balance()))
        t.sleep(3)
        show_menu()
        

def Sam():
    global rec
    sam =0
    for i in range(len(rec)):
        rec[i]=list(rec[i])
        tec = rec[i]
        sam+=tec[3]*tec[2]
    return sam

def Balance():
    global log
    rowP = BD.Row("Player",(log),"S")
    rowP = rowP[0]
    return rowP[4]