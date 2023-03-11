from datetime import date

def cheque(ingr,sum):
    my_file = open("cheque.{0}.txt".format(date.today()), "w+")
    my_file.write("Чек!")
    ing = "Ингридиенты"
    num = 0
    n=0
    for i in range(len(ingr)):
        ingr[i]=list(ingr[i])
        tec = ingr[i]
        ing=tec[1]
        num=tec[2]
        my_file.write("{0}. {1}  шт:{2}".format(ing,num))        
        n+=1
    my_file.write()
    my_file.write("Цена: "+str(sum))
    my_file.close()