import Registration
import os
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
    print("Nice!")