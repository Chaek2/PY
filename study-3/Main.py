import os, AdminMenu, Registration,BD, PlayerMenu
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
        options = ['Купить', 'Выйти']
        option, index = pick(options, title, indicator='=>')
        if(index==0):
            PlayerMenu.BuyComponent(log)
        if(index==1):
            exit()
    else:
        rec = BD.Row("History_Buy",BD.Row("Player",(log),"S"),"S")
        if not rec:
            title = 'Меню пользователя: '
            options = ['Купить']
            option, index = pick(options, title, indicator='=>')
            PlayerMenu.BuyComponent(log)
        else:
            title = 'Меню пользователя: '
            options = ['Купить', 'Выйти']
            option, index = pick(options, title, indicator='=>')
            if(index==0):
                PlayerMenu.BuyComponent(log)
            if(index==1):
                exit()
            