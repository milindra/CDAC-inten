import mysql.connector #for database connectivity

con=mysql.connector.connect(user="root",password="",host="localhost",database="test")
cur=con.cursor()
cur.execute("insert into xyz values(19)");

print('one row inserted')

print(cur.rowcount)

con.commit()

cur.close()
con.close()
