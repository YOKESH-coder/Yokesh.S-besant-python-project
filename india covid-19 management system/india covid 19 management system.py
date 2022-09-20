
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sanjay sa",
    database = "covid"
)

mycursor = db.cursor()

#creating database
#mycursor.execute("create database covid")
#print("DATABASE CREATED SUCCESSFULLY")

#creating table chennai
#mycursor.execute("create table chennai(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)")
#print("TABLE CREATED SUCCESSFULLY")

#creating table bangalore
#mycursor.execute("create table bangalore(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)")
#print("TABLE CREATED SUCCESSFULLY")

#creating table maharashtra
#mycursor.execute("create table maharashtra(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)");
#print("TABLE CREATED SUCCESSFULLY")

#creating table kerala
#mycursor.execute("create table kerala(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)");
#print("TABLE CREATED SUCCESSFULLY")

#creating table delhi
#mycursor.execute("create table delhi(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)");
#print("TABLE CREATED SUCCESSFULLY")

#creating table bihar
#mycursor.execute("create table bihar(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)");
#print("TABLE CREATED SUCCESSFULLY")

#creating table hydrabad
#mycursor.execute("create table hydrabad(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)");
#print("TABLE CREATED SUCCESSFULLY")

#creating table karnataka
#mycursor.execute("create table karnataka(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)")
#print("TABLE CREATED SUCCESSFULLY")

#creating table punjab
#mycursor.execute("create table punjab(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)")
#print("TABLE CREATED SUCCESSFULLY")

#CREATING TABLE GOA
#mycursor.execute("create table goa(NAME varchar(50), AGE int, STAGE varchar(50), MOBILE int)")
#print("TABLE CREATED SUCCESSFULLY")

print("                                 COVID-19 MANAGEMENT SYSTEM(INDIA)\n")

def AFFECT():
    print("DONT'T WORRY WE WILL MAKE YOU CURE SURE\n")
    b = str(input("ENTER YOUR STATE: ")).lower().strip()
    if b == 'bangalore':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into bangalore(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'bihar':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into bihar(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'delhi':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into delhi(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")   

    elif b == 'goa':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into goa(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'hydrabad':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into hydrabad(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'karnataka':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into karnataka(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'kerala':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into kerala(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'maharashtra':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into maharashtra(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'punjab':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into punjab(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    elif b == 'tamilnadu':
        c = str(input("ENTER YOUR NAME: ")).upper().strip()
        d = int(input("ENTER YOUR AGE: "))
        e = str(input("ENTER THE STAGE WHETHER NORMAL OR CRITICAL: ")).upper().strip()
        f = int(input("ENTER YOUR MOBILE NUMBER: "))
        sql = ("insert into tamilnadu(NAME, AGE, STAGE, MOBILE) values(%s,%s,%s,%s)")
        val = (c, d, e, f)
        mycursor.execute(sql,val)
        db.commit()
        print(f"REGISTERED AND DON'T WORRY {c} AND YOU WILL GET ALRIGHT SOON")

    else:
        print("PLEASE ENTER FROM THE STATES BELOW")
        g = ['TAMILNADU', 'BANGALORE', 'BIHAR', 'DELHI', 'GOA', 'HYDRABAD', 'KARNATAKA', 'KERALA', 'MAHARASHTRA', 'PUNJAB']
        for i in g:
            print(i)
        AFFECT()

def RECOVER():
    print("YOU ARE RECOVERED FROM VIRUS, PLEASE FILL THE DETAILS BELOW")
    h = str(input("ENTER YOUR STATE: ")).lower().strip()
    if h == 'bangalore':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from bangalore where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'bihar':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from bihar where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'delhi':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from delhi where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'goa':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from goa where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'hydrabad':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from hydrabad where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")        

    elif h == 'karnataka':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from karnataka where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'kerala':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from kerala where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'maharashtra':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from maharashtra where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'punjab':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from punjab where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    elif h == 'tamilnadu':
        i = str(input("ENTER YOUR NAME: ")).upper().strip()
        j = int(input("ENTER YOUR REGISTERED NUMBER: "))
        sql = ("delete from tamilnadu where NAME = %s and MOBILE  = %s")
        val = (i,j)
        mycursor.execute(sql,val)
        db.commit()
        print("SUCCESSFULLY REMOVED")

    else:
        print("PLEASE ENTER FROM THE STATES BELOW")
        g = ['TAMILNADU', 'BANGALORE', 'BIHAR', 'DELHI', 'GOA', 'HYDRABAD', 'KARNATAKA', 'KERALA', 'MAHARASHTRA', 'PUNJAB']
        for i in g:
            print(i)  
        RECOVER()

def ACTIVE_CASE():
    k = str(input("PLEASE ENTER YOUR STATE: ")).lower().strip()
    if k == 'bangalore':
        mycursor.execute("select * from bangalore")
        for i in fetch:
            print(i)
    elif k == 'bihar':
        mycursor.execute("select * from bihar")
        for i in fetch:
            print(i)
    elif k == 'delhi':
        mycursor.execute("select * from delhi")
        for i in fetch:
            print(i)
    elif k == 'goa':
        mycursor.execute("select * from goa")
        for i in fetch:
            print(i)
    elif k == 'hydrabad':
        mycursor.execute("select * from hydrabad")
        for i in fetch:
            print(i)
    elif k == 'karnataka':
        mycursor.execute("select * from karnataka")
        for i in fetch:
            print(i)
    elif k == 'kerala':
        mycursor.execute("select * from kerala")
        for i in fetch:
            print(i)
    elif k == 'maharashtra':
        mycursor.execute("select * from karnataka")
        for i in fetch:
            print(i)
    elif k == 'punjab':
        mycursor.execute("select * from punjab")
        for i in fetch:
            print(i)
    elif k == 'tamilnadu':
        mycursor.execute("select * from tamilnadu")
        fetch = mycursor.fetchall()
        for i in fetch:
            print(i)
    else:
        print("PLEASE ENTER THE STATE FROM BELOW LIST")
        Y = ['TAMILNADU', 'BANGALORE', 'BIHAR', 'DELHI', 'GOA', 'HYDRABAD', 'KARNATAKA', 'KERALA', 'MAHARASHTRA', 'PUNJAB']
        for i in Y:
            print(i)  
        ACTIVE_CASE
        
print("ARE YOU AFFECTED, RECOVERED, OR YOU WANT TO SEE NUMBER OF CASES IN COVID")
a = int(input("TYPE 1 IF YOU ARE AFFECTED\nTYPE 2 IF YOU ARE RECOVERED\nTYPE 3 IF YOU WANNA SEE THE ACTIVE CASES\n"))
if a == 1:
    AFFECT()
elif a == 2:
    RECOVER()
elif a == 3:
    ACTIVE_CASE()
else:
    print("\nPLEASE TYPE THE CORRESPONDING NUMBERS\n1\n2\n3")

