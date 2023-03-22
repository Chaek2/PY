import BD,Main,pick,os, random
import keyboard,Cheque
import time as t
selected = 1
column = 2
global rec,rows,log,res

def BuyComponent(_log):
    global rec,rows,log,res
    log=_log
    titles = 'Еда: '
    options=['Выйти']
    for row in BD.Row("Dish",[],"S"):
        options.append(row[1])
    option, index = pick.pick(options, titles, indicator='=>')
    if index == 0:
        Main.menu(log)
    rows = BD.Row("Component",(option),"S")
    rec = list(BD.Row("Component",[],"S"))
    res = list(BD.Row("Component",[],"S"))
    Component()

def Component():
    os.system('cls')
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('right', right)
    keyboard.add_hotkey('left', left)
    keyboard.add_hotkey('enter', enter)
    keyboard.add_hotkey('i', i)
    keyboard.add_hotkey('o', o)
    keyboard.add_hotkey('l', l)
    keyboard.wait()

def show_menu():
    global selected,rec
    os.system('cls')
    print("Ингридиенты:")
    print()
    for i in range(len(rec)):
        print("{0} {2} {3}\t {4}{5} {6}\t {7}{8} {9}\t {10}{11} {12}\t {13} {1}".format(">" if selected == i else " ", "<" if selected == i else " ",
                                                                                              ">" if column == 1 and selected == i else " ",rec[i][1],"<" if column == 1 and selected == i else " ",
                                                                                              ">" if column == 2 and selected == i else " ",rec[i][2],"<" if column == 2 and selected == i else " ",
                                                                                              ">" if column == 3 and selected == i else " ",rec[i][3],"<" if column == 3 and selected == i else " ",
                                                                                              ">" if column == 4 and selected == i else " ",rec[i][4],"<" if column == 4 and selected == i else " "))
    print()

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
    global rec,selected,column   
    rec[selected]=list(rec[selected])
    tec = rec[selected]
    if column>1:
        if(tec[2]<tec[4] and column==2):
            tec[2]+=1
        if(column==3):
            tec[3]+=1
        if(column==4):
            tec[4]+=1
    else:
        return
    show_menu()

def left():
    global rec,selected,column   
    rec[selected]=list(rec[selected])
    tec = rec[selected]
    if column>1:
        if(tec[2]>0 and column==2):
            tec[2]-=1
        if(column==3 and tec[3]>0):
            tec[3]-=1
        if(column==4 and tec[4]>0):
            tec[4]-=1
    else:
        return
    show_menu()

def l():
    global column,rec,selected
    if column != 1:
        return
    title = input("Введите название блюда: ")    
    d = input()    
    rec[selected]=list(rec[selected])
    tec = rec[selected]
    tec[1]=title
    show_menu()
#-
def i():
    global column,rec
    if column == 1:
        return
    column -= 1
    show_menu()
#+
def o():
    global column,rec
    if column == 4:
        return
    column += 1
    show_menu()

def enter():
    global res,rec,log
    summary =0
    for i in range(0,len(rec)):
        res[i]=list(res[i])
        rec[i]=list(rec[i])
        rec1=rec[i]
        res1=res[i]
        if res1[4]<rec1[4]:
            summary += (rec1[4]-res1[4])*rec1[3]
    if Balance() < summary:
        return
    BD.BuyComponent(log,summary)
    BD.AddSkald(rec)
    Main.menu(log)
        
def Balance():
    global log
    rowP = BD.Row("Player",(log),"S")
    rowP = rowP[0]
    return rowP[4]