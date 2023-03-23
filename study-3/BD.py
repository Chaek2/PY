import sqlite3 as sl
import random as r
from datetime import date
import time


def Row(table,record,fun):
    con = sl.connect('study-3\Yout.db')
    cur = con.cursor()
    match table:
        case "Player":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Number,Password) values (?,?)',(record[0],record[1]))
                con.commit()
            elif(fun=="U"):
                cur.execute('Update '+table+' set Number = ?,Password = ?,Card = ?, Wallet = ? where ID_Player = ?',(record[0],record[1],record[2],record[3],record[4]))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Player = ?',[record]) 
                con.commit()          
            elif(fun=="S"):
                if not record:
                    return cur.execute('Select * from '+table).fetchall()
                else:
                    return cur.execute('Select * from '+table+' where Number = ?',[record]).fetchall()
        case "Component":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Title,Num,Price,Sklad) values (?,?,?,?)',(record[0],record[1],record[2],record[3]))
                con.commit()                
            elif(fun=="U"):
                cur.execute('Update '+table+' set Title = ?,Num = ?,Price = ?, Sklad=? where ID_Component = ?',(record[0],record[1],record[2],record[3],record[4]))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Component = ?',[record])    
                con.commit()
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall()
                else:
                    return cur.execute('Select Component.ID_Component,Component.Title,Component.Num,Component.Price,Component.Sklad from Component inner join Dish_Component on Dish_Component.Component_ID = Component.ID_Component inner join Dish on Dish.ID_Dish = Dish_Component.Dish_ID where Dish.Title = ?',[record]).fetchall()
            elif(fun=="SE"): 
                    return cur.execute('Select * from '+table +' where ID_Component = ?',[record]).fetchall()
        case "Dish":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Title) values (?)',[record])
                con.commit()
            elif(fun=="U"):
                cur.execute('Update '+table+' set Title = ? where ID_Dish = ?',(record[0],record[1]))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Dish = ?',[record])  
                con.commit()
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall()
                else:
                    return cur.execute('Select * from '+table+' where Title = ?',[record]).fetchall()                         
        case "History_Buy":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Player_ID,Data,Sum) values (?,?,?)',(record[0],record[1],record[2]))
                con.commit()
            elif(fun=="U"):
                cur.execute('Update '+table+' set Player_ID = ?,Data = ?,Sum = ? where ID_History_Buy = ?',(record[0],record[1],record[2],record[3]))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_History_Buy = ?',[record])  
                con.commit() 
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall()
                else:
                    return cur.execute('Select * from '+table+' where Player_ID = ?',[record]).fetchall()                  
        case "Dish_Component":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Dish_ID,Component_ID) values (?,?)',(record[0],record[1]))
                con.commit()
            elif(fun=="U"):
                cur.execute('Update '+table+' set Dish_ID = ?,Component_ID = ? where ID_Dish_Component = ?',(record[0],record[1],record[2]))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Dish_Component = ?',[record]) 
                con.commit()   
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall()
                else:
                    return cur.execute('Select * from '+table+' where ID_Dish = ?',[record]).fetchall()   
                
def AddMoney(log):
    mon=0
    con = sl.connect('study-3\Yout.db')
    cur = con.cursor()
    for i in cur.execute('select * from Dish_Component inner join Component on Component.ID_Component = Dish_Component.Component_ID  where Dish_ID = 1 ').fetchall():
        mon+=i[6]*i[5]
    money = r.randint(20,40)*(mon/100)
    for i in Row("Player",log,"S"):
        Row("Player",(i[1],i[2],i[3],money,i[0]),"U")

def UpdateBalance(log, sum):
    card=0
    for i in Row("Player",(log),"S"):        
        match i[3]:
            case 0:
                print("нету карты")
                Balance=0
            case 1:
                print("бронзовая карта 5%")
                Bal=sum
                Balance = Bal/100*5
                sum-=Bal/100*5  
            case 2:
                print("серебренная карта 10%")
                Bal=sum
                Balance = Bal/100*10
                sum-=Bal/100*10  
            case 3:
                print("золотая карта 20%")
                Bal=sum
                Balance = Bal/100*20  
                sum-=Bal/100*20     
        if(sum>=5000):
            card=1
        elif(sum>=15000):
            card=2
        elif(sum>=25000):
            card=3
        else:   
            card=0
        bala = i[4]
        bala-=sum       
        bala+=Balance 
        k = Row("History_Buy",(i[0]),"S")
        if len(k)>5:
            Bal=sum            
            bala += Bal/100*20  
            sum-=Bal/100*20  
            print("Скидка 20% за более 5-ти заказов")
        if(i[3]<card):
            Row("Player",(i[1],i[2],card,bala,i[0]),"U")
        else:
            Row("Player",(i[1],i[2],i[3],bala,i[0]),"U")
        Buy(i[0],bala)
    for i in Row("Player","89680623972","S"):
        bala = i[4]
        bala+=sum
        Row("Player",(i[1],i[2],i[3],bala,i[0]),"U")
    

def Buy(id,sum):
    Row("History_Buy",[id,date.today(),sum],"I")

def UpdateSkald(ingr):
    for i in range(0,len(ingr)):
        ingr[i]=list(ingr[i])
        tec = ingr[i]
        for s in Row("Component",(tec[0]),"SE"):
            Row("Component",[s[1],s[2],s[3],tec[4]-tec[2],s[0]],"U")

def AddSkald(ingr):
    for i in range(0,len(ingr)):
        ingr[i]=list(ingr[i])
        tec = ingr[i]
        for s in Row("Component",(tec[0]),"SE"):
            Row("Component",[tec[1],tec[2],tec[3],tec[4],s[0]],"U")

def BuyComponent(log, sum):
        for i in Row("Player",(log),"S"):   
            Row("Player",(i[1],i[2],i[3],i[4]-sum,i[0]),"U")