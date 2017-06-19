from mysql.connector import MySQLConnection, Error

def insert_book(title):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='test',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
        
    query = "INSERT INTO xyz " \
            "VALUES(%s)"
    args = (title)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   insert_book(8)
 
if __name__ == '__main__':
    main()
