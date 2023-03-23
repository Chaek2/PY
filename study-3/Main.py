import os, AdminMenu, Registration,BD, PlayerMenu, Wallet, Info
from pick import pick
ranIn=100

def Auto():
    os.system('cls')
    vop = input("Автовотизироваться? [Y/N]")
    if(vop=="Y"or vop=="Yes"or vop=="y"or vop=="yes"or vop=="Д"or vop=="Да"or vop=="д"or vop=="да"):
        Registration.autorisathion()
    elif(vop=="N"or vop=="No"or vop=="n"or vop=="no"or vop=="Нет"or vop=="нет"or vop=="Н"or vop=="н"):
        Registration.registr()
    else:
        print("Нет такого ответа")
        Auto()

def menu(log):
    os.system('cls')
    if log == "89680623972":
        title = 'Меню админа: '
        options = ['Склад','Просмотр клиента', 'Выйти']
        option, index = pick(options, title, indicator='=>')
        if(index==0):
            AdminMenu.BuyComponent(log)
        if(index==1):
            Info.adminmenu()
        if(index==2):
            exit()
    else:
        rec = BD.Row("Player",(log),"S")
        for i in BD.Row("Player",(log),"S"):
            rec = BD.Row("History_Buy",i[0],"S")
        if not rec:
            for i in BD.Row("Player",(log),"S"):
                if i[4]>0:
                    PlayerMenu.BuyComponent(log)
            title = 'Меню пользователя: '
            options = ['Пополнить']
            option, index = pick(options, title, indicator='=>')
            if(index==0):
                Wallet.Add(log)
        else:
            title = 'Меню пользователя: '
            options = ['Купить', 'Пополнить','Просмотр покупок','Выйти']
            option, index = pick(options, title, indicator='=>')
            if(index==0):
                PlayerMenu.BuyComponent(log)
            if(index==1):
                Wallet.Add(log)
            if(index==2):
                Info.playermenu(log)
            if(index==3):
                exit()
            
