import sqlite3 as sl
con = sl.connect('p50-7-20-Ogurcov-Anton\study-3\Yout.db')
cur = con.cursor()

def Row(table,record,fun):
    match table:
        case "Player":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Number,Password, Wallet) values (?,?,?)',(record,))
                con.commit()
            elif(fun=="U"):
                cur.execute('Update '+table+' set Number = ?,Password = ?, Wallet = ? where ID_Player = ?',(record,))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Player = ?',(record,)) 
                con.commit()          
            elif(fun=="S"):
                if not record:
                    return cur.execute('Select * from '+table).fetchall() 
                else:
                    return cur.execute('Select * from '+table+' where Number = ?',(record,)).fetchall() 
                               
        case "Component":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Title,Num,Price) values (?,?,?)',(record,))
                con.commit()                
            elif(fun=="U"):
                cur.execute('Insert into '+table+' set Title = ?,Num = ?,Price = ? where ID_Component = ?',(record,))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Component = ?',(record,))    
                con.commit()
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall() 
                else:
                    return cur.execute('Select * from '+table+' where Title = ?',(record,)).fetchall() 
                
        case "Dish":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Title) values (?)',(record,))
                con.commit()
            elif(fun=="U"):
                cur.execute('Insert into '+table+' set Title = ? where ID_Dish = ?',(record,))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Dish = ?',(record,))  
                con.commit()
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall() 
                else:
                    return cur.execute('Select * from '+table+' where Title = ?',(record,)).fetchall()  
                          
        case "History_Buy":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Player_ID,Data,Sum) values (?,?,?)',(record,))
                con.commit()
            elif(fun=="U"):
                cur.execute('Insert into '+table+' set Player_ID = ?,Data = ?,Sum = ? where ID_History_Buy = ?',(record,))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_History_Buy = ?',(record,))  
                con.commit() 
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table).fetchall() 
                else:
                    return cur.execute('Select * from '+table+' where Player_ID = ?',(record,)).fetchall()   
                
        case "Dish_Component":
            if(fun=="I"):
                cur.execute('Insert into '+table+' (Dish_ID,Component_ID) values (?,?)',(record,))
                con.commit()
            elif(fun=="U"):
                cur.execute('Insert into '+table+' set Dish_ID = ?,Component_ID = ? where ID_Dish_Component = ?',(record,))
                con.commit()
            elif(fun=="D"): 
                cur.execute('Delete from '+table+' where ID_Dish_Component = ?',(record,)) 
                con.commit()   
            elif(fun=="S"): 
                if not record:
                    return cur.execute('Select * from '+table)
                else:
                    return cur.execute('Select * from '+table+' where ID_Dish = ?',(record,))    
