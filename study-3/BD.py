import sqlite3 as sl
import random as r
con = sl.connect('study-3\Yout.db')

cur = con.cursor()

def Row(table,record,fun):
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
                cur.execute('Insert into '+table+' set Title = ?,Num = ?,Price = ? where ID_Component = ?',(record[0],record[1],record[2],record[3]))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Component = ?',[record])    
                con.commit()
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall() 
                else:
                    return cur.execute('Select * from '+table+' where Title = ?',[record]).fetchall() 
                
        case "Dish":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Title) values (?)',[record])
                con.commit()
            elif(fun=="U"):
                cur.execute('Insert into '+table+' set Title = ? where ID_Dish = ?',(record[0],record[1]))
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
                cur.execute('Insert into '+table+' set Player_ID = ?,Data = ?,Sum = ? where ID_History_Buy = ?',(record[0],record[1],record[2],record[3]))
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
                cur.execute('Insert into '+table+' set Dish_ID = ?,Component_ID = ? where ID_Dish_Component = ?',(record[0],record[1],record[2]))
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
    for i in con.execute('select * from Dish_Component inner join Component on Component.ID_Component = Dish_Component.Component_ID  where Dish_ID = 1 ').fetchall():
        mon+=i[6]*i[5]
    money = r.random(20,40)*(mon/100)
    for i in Row("Player",log,"S"):
        Row("Player",(i[1],i[2],i[3],money))
