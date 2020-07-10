import mysql.connector
try:
    sql = "CREATE DATABASE ICICI_INTERNETBANKING"
    # sql = "CREATE DATABASE CSV_OPERATIONS"
    con = mysql.connector.connect(host="localhost",user="root",passwd="")
    cursor = con.cursor()
    cursor.execute(sql)
    print("Successfully..............")
except mysql.connector.DatabaseError as msg:
    if con:
        con.rollback()
        print("There is an exception....")
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()