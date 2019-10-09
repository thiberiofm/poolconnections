import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling


# creating MySQL DB with default credentials
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS pool_db")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

print("The DB Name MySQL connector is", mydb)

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="connection_pool",
                                                                  pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host='localhost',
                                                                  database='pool_db',
                                                                  user='root',
                                                                  password='pass')
 
    print ("Printing connection pool properties ")
    print("Connection Pool Size - ", connection_pool.pool_size)
    print("Connection Pool Name - ", connection_pool.pool_name)

    # Get connection object from a pool
    connection_object = connection_pool.get_connection()


    if connection_object.is_connected():
       db_Info = connection_object.get_server_info()
       print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)

       cursor = connection_object.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)

except Error as e :
    print ("Error while connecting to MySQL using Connection pool ", e)
finally:
    #closing database connection.
    if(connection_object.is_connected()):
        cursor.close()
        connection_object.close()
        print("MySQL connection is closed")




