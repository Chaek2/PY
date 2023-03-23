from datetime import date

def cheque(ingr,sum):
    my_file = open("cheque.{0}.txt".format(date.today()), "w+")
    my_file.write("Чек!\n\n")
    ing = "Ингридиенты"
    num = 0
    n=1
    for i in range(len(ingr)):
        ingr[i]=list(ingr[i])
        tec = ingr[i]
        ing=tec[1]
        num=tec[2]
        price=tec[3]
        my_file.write("{0}. {1}  шт:{2}  цена:{3}\n".format(n,ing,num,price))        
        n+=1
    my_file.write("")
    my_file.write("Цена: "+str(sum))
    my_file.close()