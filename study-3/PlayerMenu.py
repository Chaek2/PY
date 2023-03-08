import BD,Main,pick,os
import keyboard
selected = 1

def BuyComponent():
        title = 'Еда: '
        options=[]
        for row in BD.Row("Dish",options,"S"):
            options.append(row[1])
        option, index = pick.pick(options, title, indicator='=>')
        
        Component()

def Component():
    
    os.system('cls')

    
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.wait()

def show_menu():
        global selected
        os.system('cls')
        print("Choose an option:")
        for i in range(1, 5):
            print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()


BuyComponent()