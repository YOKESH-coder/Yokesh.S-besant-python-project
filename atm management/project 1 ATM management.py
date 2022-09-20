#                                   ATM MANAGEMENT SYSTEM
from ast import Str
from ctypes.wintypes import INT
import mysql.connector

a=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sanjay sa",
    database = "atm"
)

mycursor = a.cursor()

#creating database
#mycursor.execute("create database atm")
#print("database created successfully")

#creating table
#mycursor.execute("create table member_details(NAME varchar(40), ACCOUNT_NUMBER int, BANK_NAME varchar(50), BALANCE_AMOUNT int)")
#print("table created successfully")

#creating column1
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("YOKESH", 1234567890, "INDIAN OVERSEAS BANK", 50000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column2
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("GOPI", 1234567891, "INDIAN BANK", 30000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column3
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("RAGUL BALAJI", 1234567892, "CANARA BANK", 90000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column4
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("MUTHAMIL SELVAM", 1234567895, "BANK OF BARODA", 150000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column5
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("HARIDOSS", 1234567810, "BANK OF INDIA", 140000)
#mycursor.execute(sql,val)  
#a.commit()
#print("data added successfully")

#creating column6
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("VIGNESH", 1234787890, "STATE BANK OF HYDRABAD", 90000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column7
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("AKSHAYA", 1234567111, "INDIAN OVERSEAS BANK", 50000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column8
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("SANJAY", 1634567890, "PUNJAB NATIONAL BANK", 160000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

##creating column9
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("VENKAT", 1734567890, "BANK OF BARODA", 130000)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

#creating column10
#sql = "insert into member_details (NAME, ACCOUNT_NUMBER, BANK_NAME, BALANCE_AMOUNT) values (%s, %s, %s, %s)"
#val = ("AKSHAY", 1236367890, "STATE BANK OF INDIA", 2)
#mycursor.execute(sql,val)
#a.commit()
#print("data added successfully")

def CREDIT():
    print("ENTER THE PIN NUMBER")
    k=str(input("")).strip()
    l = str(input("DUE TO ISSUE YOU CAN ONLY ENTER THE AMOUNT 10,000 IF OKAY ENTER OKAY:")).upper().strip()
    if l == 'OKAY':
        print("PLACE YOUR MONEY INSIDE")
        m = str(input("ENTER YOUR NAME:")).upper().strip()
        if m == "YOKESH":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'YOKESH'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "GOPI":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'GOPI'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "RAGUL BALAJI":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'RAGUL BALAJI'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "MUTHAMIL SELVAM":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'MUTHAMIL SELVAM'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "HARIDOSS":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'HARIDOSS'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "VIGNESH":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'VIGNESH'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY")   
        elif m == "SANJAY":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'SANJAY'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "AKSHAYA":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'AKSHAYA'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "VENKAT":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'VENKAT'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        elif m == "AKSHAY":
            SQL = "update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT + 10000 where NAME = 'AKSHAY'"
            mycursor.execute(SQL) 
            a.commit()
            print("AMOUNT ADDED SUCCESSFULLY") 
        else:
            print("PLEASE ENTER YOUR VALID NAME")
            CREDIT()
    else:
        print("SORRY FOR THE INCONVENIENCE WE WILL MAKE THE ISSUE CLEAR ASAP")

def WITHDRAW():
    print("YOU CAN WITHDRAW THE CORRESPONING AMOUNT")
    A = [1000, 500, 100]
    for i in A:
        print(i)
    B = int(input("ENTER THE AMOUNT FROM 1000,500,100 : "))
    if B in A:
        if B == 1000:
            D = int(input("PLEASE ENTER YOUR PIN NUMBER:"))
            C = int(input("ONCE AGAIN ENTER YOUR ACCOUNT NUMBER: "))
            if C == 1234567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")
            elif C == 1234567891:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234567891")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")            
            elif C == 1234567892:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234567892")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234567895:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234567895")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234567810:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234567810")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234787890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234787890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1634567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1634567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1234567111:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1234567111")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1734567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1734567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1236367890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-1000 where ACCOUNT_NUMBER = 1236367890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            else:
                print("ENTER THE VALID ACCOUNT NUMBER:")
                WITHDRAW()

        elif B == 500:
            D = int(input("PLEASE ENTER YOUR PIN NUMBER:"))
            C = int(input("ONCE AGAIN ENTER YOUR ACCOUNT NUMBER: "))
            if C == 1234567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")
            elif C == 1234567891:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234567891")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")            
            elif C == 1234567892:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234567892")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234567895:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234567895")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234567810:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234567810")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234787890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234787890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1634567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1634567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1234567111:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1234567111")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1734567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1734567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1236367890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-500 where ACCOUNT_NUMBER = 1236367890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            else:
                print("ENTER THE VALID ACCOUNT NUMBER:")
                WITHDRAW()
        else:
            D = int(input("PLEASE ENTER YOUR PIN NUMBER:"))
            C = int(input("ONCE AGAIN ENTER YOUR ACCOUNT NUMBER: "))
            if C == 1234567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")
            elif C == 1234567891:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234567891")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")            
            elif C == 1234567892:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234567892")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234567895:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234567895")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234567810:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234567810")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD")  
            elif C == 1234787890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234787890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1634567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1634567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1234567111:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1234567111")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1734567890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1734567890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            elif C == 1236367890:
                mycursor.execute("update member_details set BALANCE_AMOUNT = BALANCE_AMOUNT-100 where ACCOUNT_NUMBER = 1236367890")
                a.commit()
                print("AMOUNT DEBITED SUCCESSFULLY")
                print("THANK YOU FOR BANKING WITH US")
                print("PLEASE REMOVE YOUR CARD") 
            else:
                print("ENTER THE VALID ACCOUNT NUMBER:")
                WITHDRAW()       
            
    else:
        print("PLEASE SELECT FROM THE CORRESPONDING AMOUNT")
        print(A)
        WITHDRAW()

def BALANCE_ENQUIRY():
    Z = [1234567890, 1234567891, 1234567892, 1234567895, 1234567810, 1234787890, 1634567890, 1234567111, 1734567890, 1236367890]
    hi = int(input("FOR BALANCE ENQUIRY PLEASE ENTER YOUR ACCOUNT NUMBER ONCE AGAIN : "))
    pin = int(input("PLEASE ENTER YOUR PIN NUMBER : "))
    if hi in Z:
        if hi == 1234567890:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234567890")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1234567891:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234567891")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")        
        elif hi == 1234567892:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234567892")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1234567895:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234567895")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1234567810:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234567810")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1234787890:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234787890")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1634567890:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1634567890")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1234567111:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1234567111")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        elif hi == 1734567890:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1734567890")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
        else:
            mycursor.execute("select BALANCE_AMOUNT from member_details where ACCOUNT_NUMBER = 1236367890")
            fetch = mycursor.fetchall()
            print(fetch)
            print("THANK YOU FOR BANKING WITH US")
    else:
        print("PLEASE ENTER THE VALID ACCOUNT NUMBER : ")
        BALANCE_ENQUIRY()


print("                                                           INSERT YOUR CARD")
print("ENTER THE STATUS OF THE CARD SHOWN IN THE DISPLAY")
print("OKAY")
print("NOT OKAY")
b = str(input("")).strip().upper()
if b == "OKAY":
    d = [1234567890, 1234567891, 1234567892, 1234567895, 1234567810, 1234787890, 1634567890, 1234567111, 1734567890, 1236367890]
    c = int(input("PLEASE ENTER YOUR ACCOUNT NUMBER:"))
    if c in d:
        if c == 1234567890:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234567890")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c == 1234567891:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234567891")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c == 1234567892:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234567892")
            e = mycursor.fetchall()
            for i in e:
                print(i) 
        elif c == 1234567895:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234567895")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c == 1234567810:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234567810")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c == 1234787890:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234787890")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c ==  1634567890:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1634567890")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c == 1234567111:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1234567111")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        elif c == 1734567890:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1734567890")
            e = mycursor.fetchall()
            for i in e:
                print(i)
        else:
            print("WELCOME")
            mycursor.execute("select NAME, ACCOUNT_NUMBER, BANK_NAME from member_details where ACCOUNT_NUMBER = 1236367890")
            e = mycursor.fetchall()
            for i in e:
                print(i)      
        print("WHAT YOU WANNA DO")
        f = ["CREDIT", "WITHDRAW", "BALANCE_ENQUIRY"]
        for i in f:
            print(i)                        
        g = str(input("")).strip().upper()
        if g == "CREDIT":
            CREDIT()
        elif g == "WITHDRAW":
            WITHDRAW()
        elif g == "BALANCE_ENQUIRY":
            BALANCE_ENQUIRY()              
        else:
            print("ONLY 3 OPTIONS AVAILABLE SELECT WITHIN THIS")                                                                           
    else:
        print("ENTER THE VALID ACCOUNT NUMBER IF SAME ISSUE ARISES PASS THE QUERY TO YOUR BANK")
else:
    print("MAY BE YOUR CARD IS EXPIRED PLEASE GO VISIT THE BANK AND CHECK IT OUT")