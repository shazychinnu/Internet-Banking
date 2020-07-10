# import mysql.connector
# # import csv
# try:
#     con = mysql.connector.connect(host="localhost",user="root",password="",database="ICICI_INTERNETBANKING")
#     # sql = "select * from request"
#     cursor = con.cursor()
#     cursor.execute("select * from request")
#     data = cursor.fetchall()
#     print(data)
#     for row in data:
#         print("Employe Name:",row)
# except mysql.connector.DatabaseError as msg:
#       if con:
#          con.rollback()
#          print("There is an Exception: ",msg)
# finally:
#     # if (con.is_connected()):
#     #     con.close()
#     #     cursor.close()
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
##########################################
import mysql.connector
import csv
try:
    sql="UPDATE employee SET salary=salary*0.20"
    con=mysql.connector.connect(host="localhost",user="root",password="",database="sennu")
    cursor=con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.execute("select * from employee")
    data=cursor.fetchall()
    for row in data:
         print("empid is:",row[0])
         print("empname is:",row[1]) 
         print("salary  is:",row[2]) 
         print("dept is:",row[3])
         print("title is:",row[4]) 
         print()
         print()
         with open('metadata1.csv', 'w', newline='') as f_handle:
              writer = csv.writer(f_handle)
              header = ['empid', 'empname' ,'salary' ,'dept' ,'title']
              writer.writerow(header)
              for row in data:
                  writer.writerow(row)
except mysql.connector.DatabaseError as msg:
      if con:
         con.rollback()
         print("it except")
finally:
      if cursor:
         cursor.close()
      if con:
         con.close()
