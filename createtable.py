import mysql.connector
try:
    sql1 = "CREATE TABLE ACCINFORMATION(datetime VARCHAR(30),acc_no INT(20),name VARCHAR(40),branch VARCHAR(30),a_balance FLOAT(10),withdraw_limit FLOAT(10),POS_limit FLOAT(10),cheque_book INT(15),debit_card_number INT(25))"
    sql2 = "CREATE TABLE CUSTOMERDETAILS(datetime VARCHAR(30),application_number INT(25),name VARCHAR(40),gender VARCHAR(20),adhar_no INT(25),pan_no VARCHAR(20),status VARCHAR(15))"
    sql3 = "CREATE TABLE TRANSACTIONS(datetime VARCHAR(30),transaction_id INT(30),type VARCHAR(25),account_number INT(30),acc_holder_name VARCHAR(40),IFSC VARCHAR(25),amount FLOAT(20),bank_name VARCHAR(30),Remaining_Balance FLOAT(20))"
    sql4 = "CREATE TABLE REQUEST(datetime VARCHAR(30),request_no INT(30),acc_no INT(30),name VARCHAR(40),amount INT(25),request_type VARCHAR(40),status VARCHAR(25))"
    sql5 = "CREATE TABLE COMPLAINTS(datetime VARCHAR(30),complaints_no INT(30),acc_number INT(25),name VARCHAR(30),email_id VARCHAR(30),complaint_details VARCHAR(100))"
    sql6 = "CREATE TABLE beneficiary_details(datetime VARCHAR(30),name VARCHAR(30),acc_no INT(25),IFSC VARCHAR(25),bank_name VARCHAR(30))"
    sql7 = "CREATE TABLE FIXED_DEPOSIT_ACCOUNT(f_acc_no INT(30),name VARCHAR(30),amount FLOAT(15),period INT(10))"
    sql8 = "CREATE TABLE INTERNET_BANKING(user_name VARCHAR(30),login_password VARCHAR(30),profile_password VARCHAR(30))"

    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
    cursor = con.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    cursor.execute(sql5)
    cursor.execute(sql6)
    cursor.execute(sql7)
    cursor.execute(sql8)
    con.commit()
    print("Successfully................")
except mysql.connector.DatabaseError as msg:
    if con:
        con.rollback()
        print("There is an exception......")
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()