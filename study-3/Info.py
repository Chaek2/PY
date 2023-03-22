import BD,Main,os

def adminmenu():
    log = input('Введите логин пользователя: ')
    logs = BD.Row("Player",(log),"S")
    if not logs:
            os.system('cls')  
            adminmenu()
    row = BD.Row("Player",(log),"S")
    for i in row:
        print("ID:{0}  Number:{1}  Password:{2}  Card:{3}  Wallet:{4}\n\n".format(i[0],i[1],i[2],i[3],i[4]))
    for i in BD.Row("Player",(log),"S"):
        row = BD.Row("History_Buy",i[0],"S")
    for i in row:
        print(str(i[2])+" | "+str(i[3])+'\n')
    l = int(input('Введите 1 для выхода: '))
    if l == 1:
        Main.menu('89680623972')
    else:
        os.system('cls')  
        adminmenu()

def playermenu(log):
    os.system('cls')
    row = BD.Row("Player",(log),"S")
    for i in BD.Row("Player",(log),"S"):
        row = BD.Row("History_Buy",i[0],"S")
    for i in row:
        print(str(i[2])+" | "+str(i[3])+'\n')
    l = int(input('Введите 1 для выхода: '))
    if l == 1:
        Main.menu(log)
    else:
        os.system('cls')  
        playermenu(log)
