import mysql.connector

def connectdb(db):
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = db
        )
    except:
        print('Error in connecting database\n')
        mydb = None

    return mydb

def selectquery(mydb):
    if(mydb is None):
        print('No such database')
        return
    
    try:
        mycursor = mydb.cursor()
        query = "select * from student where dept = 'ECE' "
        mycursor.execute(query)
        result = mycursor.fetchall()
        for x in result:
            print('---------------')
            for data in x:
                print(data)
        print('---------------')
        return result

    except:
        print('Error in selecting\n')
        return
    

#must commit the changes after inserting  

def insertdata(mydb , roll , name):
    if(mydb is None):
        print('No such database\n')
        return

    query = "insert into student (roll , sname) values (" + str(roll) + " , '" + name + "')"
    print(query)
    print()
    try:
        mycursor = mydb.cursor()
        result = mycursor.execute(query)
        mydb.commit()
    except:
        print('Error in inserting the data or data already exists\n')

#Must commit the changes after deleting

def deleterow(mydb , roll = '*'):
    if(mydb is None):
        print('No such database')
        return
    
    query = "delete from student where roll =  " + str(roll) + "  "

    try:
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
    except:
        print('Error in deleting\n')

def selectAsc(mydb):
    if(mydb is None):
        print('No such database\n')
        return
    
    query = "select * from student order by (roll) desc "

    try:
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        for x in result:
            print('---------------')
            for data in x:
                print(data)
        print('---------------')

    except:
        print('Error in selecting\n')
    

# obj = connectdb()
# insertdata(obj , 141 , 'Ravivarma')
# selectquery(obj)
# deleterow(obj , 141)