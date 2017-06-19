import mysql.connector #for database connectivity

con=mysql.connector.connect(user="root",password="",host="localhost",database="test")
cur=con.cursor()
cur.execute("SELECT COUNT(*) From xyz");
fetch=cur.fetchone();
print fetch[0]
try:
    if(cur.execute("insert into xyz values(9)")):
        print "yes";
    else:
        print "no";
except Error as error:
        print(error)
