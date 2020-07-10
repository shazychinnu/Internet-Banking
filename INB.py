# Internet Banking Process
import time
import random
import calendar
import mysql.connector
import datetime
#######################################################################
#Svings Banking Account Details
#User1
user_name = "HAZEEVALI";login_password = "hazee@12345";profile_password = "hazee@123"
#Account Details.......
acc_no = 31513532794;name = "SHAIK.HAZEEVALI";branch = "Hyderabad";a_balance = 300000.00
withdraw_limit = 50000.00 ;POS_limit =20000.00;cheque_book = [*range(54320,54370)];debit_card_number = [];#4522558866552233
complaints=[];credit_card_request = [];debit_card_request=[]
#Current Banking Account Details
#User1
c_user = "C_HAZEEVALI";c_login_password = "c_hazee@12345";c_profile_password = "c_hazee@123"
#user2
c_user2 = "C_VEERESH";c_login_password2 = "c_veeresh@12345";c_profile_password2 = "c_veeresh@123"
#Account Details.....
c_acc_no = 31213141516;c_a_balance = 30000000.00;c_name = "S.VEERESH";c_withdraw_limit = 1000000.00;c_POS_limit =200000.00
c_cheque_book = [*range(64320,64420)];c_debit_card_number = [4522312161514175];c_complaints=[];c_credit_card_request = [];c_debit_card_request=[]
#######################################################################
#IRCTC Details...........
g_seats = 60;l_seats = 30;phd_seats =10;t_seats =g_seats+l_seats+phd_seats;seats = [*range(1,101)]
t_passenger_list = [];passenger_data=[];t_user = "T_HAZEEVALI" ;t_pass= "t_hazee@12345"

# APSRTC Details.....
b_seats = 40 ; bus_seat_numbers = [*range(1,41)];bus_passenger_list =[];bus_passenger_data=[]
# OTP Validation
class account_opening:
    def __init__(self):
        pass
    def form(self):
        name = input("Enter the Name: ")
        print("1. Male  2. Female")
        option = int(input('Select the option: '))
        gender=""
        if option ==1:
            gender = "Male"
        elif option ==2:
            gender = "Female"
        adhar_no=int(input("Enter the Adhar card Number: "))
        pan_no = input("Enter the Pancard Number: ")
        print("1. Single  2. Married")
        x  = int(input("Choose the option: "))
        status=""
        if x ==1:
            status = "ACCOUNT_OPENING"
        elif x==2:
            status = "Married"
        deposit = float(input("Enter the Deposi Amount Minimum 500: "))
        now1 = datetime.datetime.now()
        noe =str(now1)
        application_number = int(random.randint(330350,999999))
        now1 = datetime.datetime.now()
        now = str(now1)
        #DATA BASE CUSTOMER INFORMATION
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
        cursor = con.cursor()
        sql = "INSERT INTO customerdetails VALUES('%s',%s,'%s','%s',%s,'%s','%s')"
        cursor.execute(sql %(now,application_number,name,gender,adhar_no,pan_no,status))
        con.commit()
        print('Your Suceessfully ompleted.....')
        open_acc_no = int(random.randint(333333000000,999999999999))
        print(open_acc_no)
        branch = "SR NAGAR"
        a_balance = deposit
        withdraw_limit = 300000.00
        POS_limit = 20000.00
        cheque_book = " "
        c_no1 = random.randint(4444,6666);c_no2 = random.randint(1111,2222);c_no3 = random.randint(0000,4444);c_no4 = random.randint(7777,9999)
        open_card_number = int(str(c_no1)+str(c_no2)+str(c_no3)+str(c_no4))
        now1 = datetime.datetime.now()
        now = str(now1)
        #DATABASE ACCOUNT INFORMATION
        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
        cursor = con.cursor()
        sql = "INSERT INTO accinformation VALUES('%s',%s,'%s','%s',%s,%s,%s,'%s',%s)"
        cursor.execute(sql %(now,open_acc_no,name,branch,a_balance,withdraw_limit,POS_limit,cheque_book,open_card_number))
        con.commit()
        print("Your Account is :",open_acc_no)
class Dice:
    globals()
    def roll(self):
        first = random.randint(0,9);second = random.randint(0,9);three = random.randint(0,9)
        four = random.randint(0,9);five = random.randint(0,9);six = random.randint(0,9)
        return (first,second,three,four,five,six)
    def otp(self):
        #validate = input("Click on submit Button: ")
        validate = "submit"
        first = time.time()
        if validate == "submit":
            otp = obj.roll()
            otp=list(otp)
            string = ""
            for i in otp:
                string+=str(i)+""
            print(string)
        enter = input("Enter the Validate OTP: ")
        print()
        if string == enter:
            time1 = time.time() - first
            if time1<=30:
                print("OTP is Validate Successfully.....!!!".center(50))
                # print("Welcome to Python World".center(50))
            else:
                print("OTP is Not Valid.......!!!!!!!!")
        else:
            print("Entered Wrong OTP Please try again....!!!!!!")
obj = Dice()        
#Create a Internet usernme and password
class create_net_banking:
    def __init__(self):
        print("Wellcome to Internet Banking Service......\U0001F64F")




    def create(self):
        #name,account_number,username,loginpassword,profilepassword
class personal_banking(Dice):
    def __init__(self):pass
        #  print("Welcome to ICICI Bank...!!!")
    class profile:
        def account_summary(self):
            print('Account Number    Branch     Available Balance ')
            print(" ",acc_no,"  ",branch,"     ",a_balance)
        def personal_info(self):
            p_pass = input("Enter profile Password: ")
            if p_pass == profile_password:
                print("Welcome Mr.Hazeevali");print("acc_no: ",acc_no);print("Branch: ",branch);print("login_password: ",login_password)
                print("Profile_password: ",profile_password)
            else:
                print("Entered Invalid Profile Password...")
        def change_password(self):
            print("1. Profile Password");print("2. Login Password")
            option = int(input("Select the required option: "))
            if option ==1:
                o_pass = input("Enter the old Profile Password: ")
                if o_pass == profile_password:
                    n_pass = input("Enter New profile Password: ")
                    profile_password = n_pass
                else:
                    print("Entered Invalid profile Password.....")
            if option == 2:
                o_pass = input("Enter the old Login Password: ")
                if o_pass == login_password:
                    n_pass = input("Enter New profile Password: ")
                    login_password = n_pass
                else:
                    print("Entered Invalid login Password....")
            else:
                print("Choose valid Option.....")
        def change_limit(self):
            print("1. Withdrawl limit");print("2. POS Limit")
            option = float(input("Choose required option: "))
            if option == 1:
                p_pass = input("Enter the Profile Password: ")
                if p_pass == profile_password:
                    limit = float(input("Enter the change Withdral limit: "))
                    withdraw_limit = limit
                else:
                    print("Enter invalid profile Password.....")
            if option == 2:
                p_pass = input("Enter the Profile Password: ")
                if p_pass == profile_password:
                    limit = float(input("Enter the change POS limit: "))
                    POS_limit = limit
                else:
                    print("Enter invalid profile Password.....")
            else:
                print("Choose valid option....")
    class transfer:
        def quick_transfer(self):
            type1= 'QUICK TRANSFER'
            name = input("Enter the Acc holder Name: ")
            acc_no = int(input("Enter the Account Number: "))
            ifsc = input("Enter the IFSC code: ")
            amount = float(input("Enter the Amount: "))
            branch = input("Enter the branch name")
            global a_balance
            balance = a_balance
            if amount <= a_balance:
                a_balance = balance - amount
                transaction_id = random.randint(3333333333,9999999999)
                now1 = datetime.datetime.now()
                now = str(now1)
                con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                cursor = con.cursor()
                sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s','%s',%s,'%s',%s)"
                cursor.execute(sql %(now,transaction_id,type1,acc_no,name,ifsc,amount,branch,a_balance))
                con.commit()
                print("Transaction is Sucessfully....");print("Remaining Balance is: ",a_balance)
            else: 
                 print("Insufficent Funds....");print("Visit Again ....!!!!!")
        def add_beneficiary(self):
            name = input("Enter the Acc holder Name: ")
            acc_no = int(input("Enter the Account Number: "))
            ifsc = input("Enter the IFSC code: ")
            bank = input("Enter the Bank Name: ")
            branch = input("Enter the branch name: ")
            obj = Dice()
            obj.otp()
            now1 = datetime.datetime.now()
            now = str(now1)
            con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
            cursor = con.cursor()
            sql = "INSERT INTO beneficiary_details VALUES('%s','%s',%s,'%s','%s')"
            cursor.execute(sql %(now,name,acc_no,ifsc,branch))
            con.commit()
            print('Account will be activated with in 24 Hours....')
        def fund_transfer(self):
            print('Coming soon....!!!!!!!!!!')
        def other_banks(self):
            print('Coming soon....!!!!!!!!!!')
    class bill_payments:
        def top_up(self):
            global a_balance
            type1 = "TOP UP"
            provider = input("Enter the provider Name: ")
            mobile_no = int(input('Enter the Mobile NUmber: '))
            print("Select Amout Rs.10 ,Rs.50,Rs.100,Rs.250,Rs.500")
            amount  = int(input("Enter the Amount: "))
            branch = input("Enter the State: ");branch = "0";ifsc = 0
            x= [10,50,100,250,500]
            for i in x:
                if amount == i:
                    if amount < a_balance:
                        a_balance = a_balance - amount
                        transaction_id = random.randint(3333333333,9999999999)
                        now1 = datetime.datetime.now()
                        now = str(now1)
                        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                        cursor = con.cursor()
                        sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                        cursor.execute(sql %(now,transaction_id,type1,mobile_no,provider,ifsc,amount,branch,a_balance))
                        con.commit()
                        print("Mobile Recharge is Successfully....")
                        break
            else:
                print('Select valid option.....!!!')
        def DTH(self):
            global a_balance
            type1 = "DTH"
            provider = input("Enter the provider Name: ")
            dth_no = int(input('Enter the Mobile NUmber: '))
            print("Select Amout Rs.100 ,Rs.500,Rs.1000,Rs.2500,Rs.5000")
            amount  = float(input("Enter the Amount: "))
            ifsc = "0";branch = input("Enter the State: ")
            x= [100,500,1000,2500,5000]
            for i in x:
                if amount == i:
                    if amount < a_balance:
                        a_balance = a_balance - amount
                        transaction_id = random.randint(3333333333,9999999999)
                        now1 = datetime.datetime.now()
                        now = str(now)
                        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                        cursor = con.cursor()
                        sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                        cursor.execute(sql %(now,transaction_id,type1,dth_no,provider,ifsc,amount,branch,a_balance))
                        con.commit()
                        print("DTH Recharge is Successfully....")
                        break
            else:
                print('Select valid option.....!!!')
        def creditcard_bill(self):
            global a_balance
            type1 = "CREDIT CARD"
            bank_name = input("Enter the Bank Name: ")
            credit_card_no = int(input("Enter the Credi card Number: "))
            c_holder_name = input("Enter the card holder Name: ")
            amount = float(input("Enter the Amount: "))
            ifsc ="0"
            if amount <= a_balance:
                a_balance = a_balance - amount
                transaction_id = random.randint(3333333333,9999999999)
                now1 = datetime.datetime.now()
                now = str(now1)
                con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                cursor = con.cursor()
                sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                cursor.execute(sql %(now,transaction_id,type1,credit_card_no,c_holder_name,ifsc,amount,bank_name,a_balance))
                con.commit()
                print('Your transaction successfully completed....')
            else:
                print("Insufficent Amount.....")
    class fixed_deposit:
        def f_display(self):
            print("1. Online");print("2. Offline")
            option=int(input("Enter the Option: "))
            if option == 1:
                contact = int(input('Enter the contact Number: '))
                obj = Dice()
                obj.otp()
                f_name = input("Enter the Name: ")
                male = input("Select the option M/F").upper()
                adhar = int(input("Enter the Adhar Number:"))
                pan = input("Enter the pan card Number: ")
                amount  = int(input("Enter the Fixed deposit Amount: "))
                print("Select the Duration :");print("1. 12 months");print("2. 24 months")
                option = int(input("Select the option: "))
                if option ==1:
                    duration = "12 Months"
                    print('Intrest rate is : 30%')
                elif option ==2:
                    duration ="24 Months"
                    print('Intrest rate is : 45%')
                print("Select your Payment method....!!!");print("1. Online");print("2. Debit/Credit Card")
                pay_type = int(input("Choose your option:"))
                if pay_type == 1:
                    user_name = input("Enter User name: ")
                    password = input('Enter your Password: ')
                    print("After cmp Transation ......")
                    print("Your transaction successfully completed..!!!!!")
                    first = random.randint(11111111111,99999999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO FIXED_DEPOSIT_ACCOUNT VALUES('%s',%s,'%s',%s,'%s')"
                    cursor.execute(sql %(now,first,f_name,amount,duration))
                    con.commit()
                    print("Your account Number is: ",first);print("aditional Information send to your registered mobile number...")
                elif pay_type ==2:
                    card_no = int(input("Enter your Card Details: "))
                    e_date = int(input("Enter your expire date: "))
                    cvv = int(input("Enter your CVV number: "))
                    name= input("Enter card holder Name: ")
                    print("Your transaction successfully completed..!!!!!")
                    first = random.randint(11111111111,99999999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO FIXED_DEPOSIT_ACCOUNT VALUES('%s',%s,'%s',%s,'%s')"
                    cursor.execute(sql %(now,first,f_name,amount,duration))
                    con.commit()
                    print("Your account Number is: ",first);print("aditional Information send to your registered mobile number...")
                else:print('Select the Valid option..!!!')
            elif option ==2:
                type1 ="FIXED DEPOSIT ACCOUNT"
                status = "In progress"
                name = input('Enter your Name: ')
                male = input("Select the option M/F").upper()
                contact = int(input('Enter your Contct mobile Number: '))
                contact2 = int(input("Enter your Contct temporary Number: "))
                amount = int(input('How much amount plan to deposit: '))
                if len(str(contact)) ==10 and len(str(contact2)) ==10:
                    if contact != contact2:
                        if male == "M":
                            print("Mr.",name,'Thank you for intrest ICICI Bank....!!!')
                        elif male == "F":
                            print("Miss.",name,'Thank you for intrest ICICI Bank....!!!');print("Our Executive will be contact shortly...")
                        now1 = datetime.datetime.now()
                        now = str(now1)
                        request_num = random.randint(111111,999999)
                        con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                        cursor = con.cursor()
                        sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s',%s,'%s','%s')"
                        cursor.execute(sql %(now,request_num,contact,name,amount,type1,status))
                        con.commit()
                    else:print("Please enter different two numbers..")
                else:print("Enter valid Contact Number..!!!")
            # option = int(input("Select the optioon:"))
    class e_service:
        def irctc(self):
            global a_balance
            global name
            name1 = name
            type1 = "IRCTC"
            t_user2 = input("IRCCTC User name: ")
            t_pass2 = input("IRCTC Password: ")
            if t_user2 == t_user and t_pass2 == t_pass:
                print("Connect to IRCTC server...")
                print("1. Hyderabad  2. Kurnool   3. Anantapur   4. Bangalore")
                t_from = int(input("From : "))
                print("1. Hyderabad  2. Kurnool   3. Anantapur   4. Bangalore")
                t_to = int(input("To : "))
                if (t_from == 1 and t_to == 4) or (t_from ==4 and t_to ==1):
                    price =1500
                elif (t_from == 1 and t_to == 2) or (t_from ==2 and t_to ==1):
                    price = 800
                elif (t_from == 1 and t_to == 3) or (t_from ==3 and t_to ==1):
                    price = 1000
                elif (t_from == 2 and t_to == 4) or (t_from ==4 and t_to ==2):
                    price = 700
                elif (t_from == 2 and t_to == 3) or (t_from ==3 and t_to ==2):
                    price = 200
                elif (t_from == 3 and t_to == 4) or (t_from ==4 and t_to ==3):
                    price = 500
                print("Select Daate: ")
                m,y=int(input("Enter the Month : ")),int(input("Enter the Year: "))
                print(calendar.month(y,m))
                no_of_seats = int(input('Enter the Number of Seats: '))
                total_price = price*no_of_seats
                ifsc ="0";branch = input("Enter the State: ")
                print(" Each Ticket Price: ",price)
                if total_price < a_balance:
                    if t_seats !=0:
                        if no_of_seats < t_seats:
                            print("1. General Seats");print("2. Ladies Resevation");print("3. Physical Handicaped")
                            quota = int(input("Enter the Special Quota: "))
                            bank_name ="0"
                            if quota ==1:
                                if g_seats !=0 :
                                    x=0
                                    while no_of_seats > x:
                                        Name = input("Enter the Name: ")
                                        age = int(input("Enter the Age: "))
                                        adhar_no = int(input("Enter the Adhar Number: "))
                                        t_passenger_list.append(name)
                                        passenger_data.extend([name,age,adhar_no])
                                        x+=1
                                    box =random.randint(1,12);box1 ="S"+str(box)
                                    ticket_no =random.randint(111101,999999)
                                    transaction_id = random.randint(4444444444,9999999999)
                                    now1 = datetime.datetime.now()
                                    now = str(now1)
                                    a_balance =a_balance -total_price
                                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                                    cursor = con.cursor()
                                    sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                                    cursor.execute(sql %(now,transaction_id,type1,ticket_no,name1,ifsc,total_price,bank_name,a_balance))
                                    con.commit()
                                    print()
                                    print("------------------------------")
                                    print("Your Tickets is Conformed....")
                                    print("From: ",t_from,"  To:",t_to)
                                    print('Your seat numbers....')
                                    num = seats[0:no_of_seats]
                                    print("Coach: ",box1)
                                    conform = str(list(zip(t_passenger_list,num)))
                                    print(conform)
                                    print("The Total Price: ",total_price)
                                    print()
                                    print("-------------------------------")
                                    print("Thanks for Visiting IRCTC....")
                                    print("-------------------------------")
                            elif quota ==2 or option ==3:
                                if l_seats !=0 or t_seats !=0 :
                                    x=0
                                    while no_of_seats > x:
                                        name = input("Enter the Name: ")
                                        age = int(input("Enter the Age: "))
                                        adhar_no = int(input("Enter the Adhar Number: "))
                                        t_passenger_list.append(name)
                                        passenger_data.extend([name,age,adhar_no])
                                        x+=1
                                    box =random.randint(1,12);box1 ="S"+str(box)
                                    print()
                                    print("------------------------------")
                                    print("Your Tickets is Conformed....")
                                    print("From: ",t_from,"  To:",t_to)
                                    print('Your seat numbers....')
                                    num = seats[0:no_of_seats]
                                    print("Coach: ",box1)
                                    conform = str(list(zip(t_passenger_list,num)))
                                    print(conform)
                                    ox =random.randint(1,12);box1 ="S"+str(box)
                                    ticket_no =random.randint(111101,999999)
                                    ticket_no =random.randint(111101,999999)
                                    transaction_id = random.randint(4444444444,9999999999)
                                    now1 = datetime.datetime.now()
                                    now = str(now1)
                                    a_balance =a_balance -total_price
                                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                                    cursor = con.cursor()
                                    sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                                    cursor.execute(sql %(now,transaction_id,type1,ticket_no,name,ifsc,total_price,bank_name,a_balance))
                                    con.commit()
                                    print("The Total Price: ",total_price)
                                    print()
                                    print("-------------------------------")
                                    print("Thanks for Visiting IRCTC....")
                                    print("-------------------------------")
                else:
                    print("Insufficient Balaance.....")
            else:
                print('Invalid username and Password....')
        def apsrtc(self):
                global a_balance;global name
                type1 = "APSRTC"
                branch = input("Enter the State: ")
                print("Connect to APSRTC server...")
                print("1. Hyderabad  2. Kurnool   3. Anantapur   4. Bangalore")
                t_from = int(input("From : "))
                print("1. Hyderabad  2. Kurnool   3. Anantapur   4. Bangalore")
                t_to = int(input("To : "))
                if (t_from == 1 and t_to == 4) or (t_from ==4 and t_to ==1):
                    price =2500
                elif (t_from == 1 and t_to == 2) or (t_from ==2 and t_to ==1):
                    price = 1200
                elif (t_from == 1 and t_to == 3) or (t_from ==3 and t_to ==1):
                    price = 1600
                elif (t_from == 2 and t_to == 4) or (t_from ==4 and t_to ==2):
                    price = 1000
                elif (t_from == 2 and t_to == 3) or (t_from ==3 and t_to ==2):
                    price = 400
                elif (t_from == 3 and t_to == 4) or (t_from ==4 and t_to ==3):
                    price = 700
                print("Select Daate: ")
                m,y=int(input("Enter the Month : ")),int(input("Enter the Year: "))
                print(calendar.month(y,m))
                no_of_seats = int(input('Enter the Number of Seats: '))
                total_price = price*no_of_seats
                ifsc ="0"
                print(" Each Ticket Price: ",price)
                if total_price < a_balance:
                    if b_seats !=0:
                        if no_of_seats < b_seats:
                            print("1. General Seats");print("3. Physical Handicaped")
                            quota = int(input("Enter the Special Quota: "))
                            if quota ==1:
                                if b_seats !=0 :
                                    x = 0
                                    while no_of_seats > x:
                                        name = input('Enter the Passanger name: ')
                                        age = int(input("Enter the passanger age: "))
                                        x+=1
                                    a_balance = a_balance - total_price
                                    num = bus_seat_numbers[0:no_of_seats]
                                    ticket_no = random.randint(111011,999999)
                                    transaction_id = random.randint(4444444444,9999999999)
                                    now1 = datetime.datetime.now()
                                    now = str(now1)
                                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                                    cursor = con.cursor()
                                    sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                                    cursor.execute(sql %(now,transaction_id,type1,ticket_no,name,ifsc,total_price,branch,a_balance))
                                    con.commit()
                                    print("Your Tickets is Conformed....")
                                    print("From: ",t_from,"  To:",t_to)
                                    print('Your seat numbers....')
                                    print("The Total Price: ",total_price)
                                    print()
                                    print("Thanks for Visiting APSRTC....")
                            elif  option ==3:
                                if b_seats !=0 :
                                    x = 0
                                    while no_of_seats > x:
                                        name = input('Enter the Passanger name: ')
                                        age = int(input("Enter the passanger age: "))
                                        x+=1
                                    a_balance = a_balance - total_price
                                    num = bus_seat_numbers[0:no_of_seats]
                                    ticket_no = random.randint(111011,999999)
                                    transaction_id = random.randint(4444444444,9999999999)
                                    now1 = datetime.datetime.now()
                                    now = str(now1)
                                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                                    cursor = con.cursor()
                                    sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                                    cursor.execute(sql %(now,transaction_id,type1,ticket_no,name,ifsc,total_price,branch,a_balance))
                                    con.commit()
                                    print("Your Tickets is Conformed....")
                                    print("From: ",t_from,"  To:",t_to)
                                    print('Your seat numbers....')
                                    print("The Total Price: ",total_price)
                                    print()
                                    print("Thanks for Visiting APSRTC....")
                else:
                    print("Insufficient Balaance.....")
    class request:
        def cheque_book_request(self):
            global acc_no;global name;global a_balance;ifsc=0
            status ="In Progress"
            type1 = "CHEQUE BOOK REQUEST"
            print("Select Account Number : ",acc_no)
            print("Enter the number of books and select the number of leaves in each book")
            m_city = input("Multi City Option Y/N").casefold()
            if m_city =="y":
                print('selected MUlticity option...')
            elif m_city == "n":
                print("Not selected Multicity option....")
            else:
                print('Select valid option....')
            num = int(input("Number of cheque Books: "))
            amount = 150.00
            print("1. 25 \n2. 50 \n3.100")
            leaves = int(input("Select Number of cheque Leaves: "))
            request_num = random.randint(111111,999999)
            now1 = datetime.datetime.now()
            now = str(now1)
            con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
            cursor = con.cursor()
            sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s',%s,'%s','%s')"
            cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
            con.commit()
            a_balance = a_balance - amount
            branch = "PEAPULLY"
            transaction_id = random.randint(4444444444,9999999999)
            now1 = datetime.datetime.now()
            now = str(now1)
            con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
            cursor = con.cursor()
            sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
            cursor.execute(sql %(now,transaction_id,type1,request_num,name,ifsc,amount,branch,a_balance))
            con.commit()
            print("Your request successfuly completed... \n Your Request number is: ",request_num)
        def DD(self):
            global a_balance
            branch = "PEAPULLY"
            option =0
            charges = 50
            type1 = 'DD REQUEST';ifsc=0
            status = "In Progress"
            while option <=3:
                p_pass = input('Enter Profile Password: ')
                if p_pass == profile_password:
                    r_address = input("Enter the Reciever Name(DD): ")
                    amount= float(input("Enter the Amount: "))
                    s_address =input("Enter Your Contact Details: ")
                    request_num = random.randint(111111,999999)
                    request_num = random.randint(111111,999999)
                    transaction_id = random.randint(4444444444,9999999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    a_balance = a_balance - (amount + charges)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s',%s,'%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,r_address,amount,type1,status))
                    con.commit()
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s',%s,%s,'%s',%s)"
                    cursor.execute(sql %(now,transaction_id,type1,acc_no,r_address,ifsc,(amount+charges),branch,a_balance))
                    con.commit()
                    print("Your request successfuly completed... \n Your Request number is: ",request_num)
                    break
                else:
                    print("Entered Invalid Profile Password...")
                option+=1
        def Stop_cheque_leaf(self):
            print("1. Stop Cheque leaf");print("2. Hold cheque leaf");print("3. Remove Hold")
            num = int(input("Select the option: "))
            amount = "NO Charge"
            type1 = "STOP CHEQUE LEAF"
            status = "In Progress"
            c_no = int(input("Enter the Cheque NUmber: "))
            if num ==1:
                if c_no in cheque_book:
                    cheque_book.remove(c_no)
                    request_num = random.randint(111111,999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s','%s','%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
                    con.commit()
                    print("Cheque Number will be Permanently Stopped...");print("Your Request number is: ",request_num)
                else:
                    print('Enter the correct cheque leaf Number')
            elif num ==2:
                type1 = "HOLD CHEQUE LEAF"
                # c_no : int(input("Enter the Cheque NUmber: "))
                if c_no in cheque_book:
                    cheque_book.remove(c_no)
                    request_num = random.randint(111111,999999)
                    request_num = random.randint(111111,999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s','%s','%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
                    con.commit()
                    print("Cheque Number will be temporary Stopped...");print("Your Request number is: ",request_num)
                else:
                    print('Enter the correct cheque leaf Number')
            elif num ==3:
                type1 = "REMOVE HOLD CHEQUE LEAF"
                # c_no : int(input("Enter the Cheque NUmber: "))
                request_no = int(input("Enter the Request Number: "))
                if c_no in cheque_book:
                    cheque_book.append(c_no)
                    request_num = random.randint(111111,999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s','%s','%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
                    con.commit()
                    print("Hold Removed....")
                else:
                    print('Enter the correct cheque leaf Number')
            else:
                print("select Invalid option...")
        def apply_credit_card(self):
            global acc_no;global name
            amount = 0
            status = "In progress"
            type1 = "CREDIT CARD APPLY"
            print("1. Credit card Apply");print("2. Credit card Status")
            option = int(input("Select the Option: "))
            if option ==1:
                print("1. Salary");print("2. savings");print("3. Corporate");print("4. Self Employe")
                relation = int(input('Enter relation with ICICI: '))
                if relation == 1 or 2 or 3 :
                    s_amount =float(input('Enter your take home Salary: '))
                    if s_amount <= 20000:
                        print("YourNot eligible to apply Credit card...")
                        exit()
                    x = int(input("Choose the option 1. Male  2. Female: "))
                    if x == 1:
                        gender = "Male"
                    else:
                        gender = "Female"
                    location = input("Enter your current location: ")
                    adhar_num = int(input('Enter the Adhar Number: '))
                    pan_num = input('Enter the Pancard Number: ')
                    request_num = random.randint(111111,999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO CUSTOMERDETAILS VALUES('%s',%s,'%s','%s',%s,'%s','%s')"
                    cursor.execute(sql %(now,request_num,name,gender,adhar_num,pan_num,type1))
                    con.commit()
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s',%s,'%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
                    con.commit()
                    print("Your request is accepted....");print("Your request number is:",request_num)
                    credit_card_request.append(request_num)
                elif relation == 4:
                    income = float(input("Enter the Your Monthly Income: "))
                    if income <= 30000:
                        print("YourNot eligible to apply Credit card...")
                        exit()
                    location = input("Enter your current location: ")
                    adhar_num = int(input('Enter the Adhar Number: '))
                    pan_num = input('Enter the Pancard Number: ')
                    x = int(input("Choose the option 1. Male  2. Female: "))
                    if x == 1:
                        gender = "Male"
                    else:
                        gender = "Female"
                    request_num = random.randint(111111,999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO CUSTOMERDETAILS VALUES('%s',%s,'%s','%s',%s,'%s','%s')"
                    cursor.execute(sql %(now,request_num,name,gender,adhar_num,pan_num,type1))
                    con.commit()
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s',%s,'%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
                    con.commit()
                    print("Your request is accepted....");print("Your request number is:",request_num)
                    redit_card_request.append(request_num)
            elif option ==2:
                credit_request_num = int(input("Enter the Request Number: "))
                if credit_card_request in credit_card_request:
                    print("Your credit card Status : Completed")
                    c_no1 = random.randint(4444,6666);c_no2 = random.randint(1111,2222);c_no3 = random.randint(3333,4444);c_no4 = random.randint(7777,9999)
                    card_number = c_no1+c_no2+c_no3+c_no4
                    cvv = random.randint(111,999)
                    date = random.randint(1,12);year=random.randint(2025,2040)
                    expire_date = str(date)+ "/"+str(year)
                    print("Mr.",name,"Your Credit Crad Details....")
                    print('Your card Credit card Number: ',c_no1,"-",c_no2,"-",c_no3,"-",c_no4)
                    print("Expire Date: ",expire_date)
                    print('CVV Number: ',cvv)
                else: 
                    print('Entered Invalid Request Number.....')

        def apply_debit_card(self):
            global a_balance;global name
            amount = 150.00
            type1 = 'DEBIT CARD  APPLY'
            status = "In progress"
            branch = "PEAPULLY"
            global name;global acc_no;ifsc = "ICICI00397"
            if debit_card_number:
                print("Your previous card is activated....\n   So please Block your previous card....")
            else:
                account_number = int(input("Enter your Account Number: "))
                print("New Debit card charges will be Rs.150")
                print("1. Continue");print("2. exit")
                option = int(input("Select the option: "))
                if option ==1:
                    a_balance = a_balance - amount
                    request_num = random.randint(111111,999999)
                    debit_card_request.append(request_num)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO TRANSACTIONS VALUES('%s',%s,'%s',%s,'%s','%s',%s,'%s',%s)"
                    cursor.execute(sql %(now,request_num,type1,acc_no,name,ifsc,amount,branch,a_balance))
                    con.commit()
                    sql = "INSERT INTO REQUEST VALUES('%s',%s,%s,'%s',%s,'%s','%s')"
                    cursor.execute(sql %(now,request_num,acc_no,name,amount,type1,status))
                    con.commit()
                    print("Your request is Accepted ,Request No: ",request_num)
                    print("Your card will be recevie with in 30 working days...")
                elif option ==2:
                    exit()
        def enquiry(self):
            print('Missed call Banking: 95946 12615')
            print("SMS Banking: 92156 76766")
            print("customer care Number: 1860 120 7777")
    class links:
        def imobile(self):
            print("i Mobile link....")
        def c_manager(self):
            print("Name: Hazeevali");print("Mobile: 91221030352");print("Hyderabad")
        def complaints(self):
            global name;global acc_no
            print("1. New Complint");print("2. Complaint Status");print("Re-open Complaint")
            option = int(input("Select the option: "))
            if option ==1:
                ac_num = int(input("Enter the Account Number: "))
                if ac_num == acc_no:
                    name = input("Enter the Nme: ")
                    email = input("Enter the Email address: ")
                    complaint = input("Enter the Complaint: ")
                    complaint_num = random.randint(111111,999999)
                    now1 = datetime.datetime.now()
                    now = str(now1)
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="ICICI_INTERNETBANKING")
                    cursor = con.cursor()
                    sql = "INSERT INTO COMPLAINTS VALUES('%s',%s,%s,'%s','%s','%s')"
                    cursor.execute(sql %(now,complaint_num,acc_no,name,email,complaint))
                    con.commit()
                    print("Your Complaint Number: ",complaint_num);print('Your complint is resolve in next 48 Hours...')
                    complaints.append(complaint_num)
            elif option ==2:
                complaint_number = int(input('Enter the Complaint Number: '))
                if complaint_number in complaints:
                    print('Complaint status is : ',"Completed")
                    complaints.remove(complaint_number)
                else:
                    print("Your Complaint number is Invalid...")
            elif option == 3:
                complaint_number = int(input('Enter the Complaint Number: '))
                if complaint_number not in complaints:
                    print("Complaint is Re-opened");print('Your complint is resolve in next 48 Hours...')
                    complaints.append(request_num)
                else:
                    print("Your Complaint number is Invalid...")
class p_service(personal_banking):
    def __init__(self):
        super().__init__()
        print()
        print("1. Profile/Summary");print("2. Transfer/Payments");print("3. Bill Payments");print("4. Fixed Deposit")
        print("5. Online Services/E_Services");print("6. Requests");print("7. Links")
        option = int(input("Choose the Required options: "))
        if option == 1:
            self.profile()
            print()
            print("1. Account Summary");print("2. Profile");print("3. Change Password");print("4. Change_limit")
            option1 = int(input("Choose the options: "))
            if option1 == 1:
                obj = self.profile()
                obj.account_summary()
            if option1 == 2:
                obj = self.profile()
                obj.personal_info()
                print()
            if option1 == 3:
                obj = self.profile()
                obj.change_password()
            if option1 == 4:
                obj = self.profile()
                obj.change_limit()
        if option ==2:
            self.transfer()
            print()
            print("1. Quick Transfer");print("2. Add Beneficiary");print("3. Fund Transfer");print("4. Other Bank Transactions")
            option1 = int(input("Choose required Option: "))
            if option1 == 1:
                obj = self.transfer()
                obj.quick_transfer()
            if option1 == 2:
                obj = self.transfer()
                obj.add_beneficiary()
                print()
            if option1 == 3:
                obj = self.transfer()
                obj.fund_transfer()
            if option1 == 4:
                obj = self.transfer()
                obj.other_banks()
        if option ==3:
            self.bill_payments()
            print()
            print("1.Mobile Top up");print("2. DTH");print("3. Credit Card Bill")
            option1 = int(input("Select required option: "))
            if option1 == 1:
                obj = self.bill_payments()
                obj.top_up()
            if option1 == 2:
                obj = self.bill_payments()
                obj.DTH()
                print()
            if option1 == 3:
                obj = self.bill_payments()
                obj.creditcard_bill()
        if option ==4:
            obj = self.fixed_deposit()
            obj.f_display()
        if option ==5:
            self.e_service()
            print()
            print("1. IRCTC");print("2. APSRTC")
            option1 = int(input("Choose the Required options: "))
            if option1 == 1:
                obj = self.e_service()
                obj.irctc()
            if option1 == 2:
                obj = self.e_service()
                obj.apsrtc()
                print()
        if option ==6:
            self.request()
            print()
            print("1. Cheque Book Request");print("2. Demand Draft");print("3. Stop cheque leaf");print("4. Apply Credit card")
            print("5. Apply Debit card");print("6. Enquiry")
            option1 = int(input("Choose the Required options: "))
            if option1 == 1:
                obj = self.request()
                obj.cheque_book_request()
            if option1 == 2:
                obj = self.request()
                obj.DD()
                print()
            if option1 == 3:
                obj = self.request()
                obj.Stop_cheque_leaf()
            if option1 == 4:
                obj = self.request()
                obj.apply_credit_card()
            if option1 == 5:
                obj = self.request()
                obj.apply_debit_card()
                print()
            if option1 == 6:
                obj = self.request()
                obj.enquiry()
        if option ==7:
            self.links()
            print()
            print("1. Imobile App");print("2. Branch Manager Contact");print("3. Complaints")
            option1 = int(input("Select required Option: "))
            if option1 == 1:
                obj = self.links()
                obj.imobile()
            if option1 == 2:
                obj = self.links()
                obj.c_manager()
                print()
            if option1 == 3:
                obj = self.links()
                obj.complaints()
    def m(self):pass
class login(p_service):
    def __init__(self):
        print("Welcome to ICICI Internet Banking...!!!!");print("1. Personal Banking");print("2. Corporate Banking");print("3. Account Opening")
        option =int(input("Select your Banking option: "))
        if option ==1:
            user = input("Enter the User Name: ")
            passwd = input("Enter the Login Password: ")
            if user == user_name and passwd == login_password:
                print(name,"Welcome to ICICI Personal Internet Banking...!!!")
                obj = p_service()
            else: 
                print("Enter valid User name & Password....!!!");print('Thankyou for visiting ICICI Bank....!!!')
        if option == 2:
            user = input("Enter the User Name: ")
            passwd = input("Enter the Login Password: ")
            if user == c_user_name and passwd == c_login_password:
                print(name,"Welcome to ICICI Corporate Internet Banking...!!!")
        if option ==3:
            print("Welcome to ICICI Banking.....")
            acc_obj = account_opening()
            acc_obj.form()
            #   obj1 = P_service()
obj = login()

""""for i in range(1,40,4):
    if i <=12:
        print(i," W","O","|", "O",i+1,"      ","O",i+2, "W","O",i+3)
    else:
        print(i,"W","O","|", "O",i+1,"     ","O",i+2, "W","O",i+3)"""