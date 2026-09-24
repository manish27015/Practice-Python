import mysql.connector
mysqldb=mysql.connector.connect(host="localhost", user="root",password="12345", database="testdataset")
mysqlcursor=mysqldb.cursor()
# TO create a table
# mysqlcursor.execute("create table studentrecord(rollno INT, name VARCHAR(30), marks INT)")
#insert into table
'''
try:
    
    mysqlcursor.execute("insert into studentrecord(rollno, name, marks) values(2, 'Raj',86 )")
    mysqldb.commit()
    print("Record inseted into the table")

except:
    mysqldb.rollback()

mysqldb.close()  
'''
# display record
'''
try:
    mysqlcursor.execute("select * from studentrecord where rollno = 1")
    result= mysqlcursor.fetchall()
    for i in result:
        roll= i[0]
        name= i[1]
        marks= i[2]
        print(roll,name,marks)
    
except:
    print("Some issue in the code")
mysqldb.close()                                
'''
#To update the record
'''
try:
    mysqlcursor.execute("update studentrecord set name ='Sachin' where rollno = 1")
    mysqldb.commit()
    print("Record update")

except: 
    mysqlcursor.rollback()
'''
# To delete the record
'''
try:
    mysqlcursor.execute("delete from studentrecord where rollno=1 ")
    mysqldb.commit()
    print("Record delete")

except: 
    mysqlcursor.rollback()
    
mysqldb.close
'''
print(mysqldb.is_connected())
mysqldb.ping()