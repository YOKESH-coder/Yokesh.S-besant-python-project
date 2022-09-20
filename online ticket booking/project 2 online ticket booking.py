from ast import Pass
from email import policy
import mysql.connector
a = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sanjay sa",
    database = "ticket_booking"
)

mycursor = a.cursor()

#creating database
#mycursor.execute("create database ticket_booking")
#print("database created successfully")

#creating table bus
#mycursor.execute("create table bus(NAME varchar(50), AGE int, DESTINATION varchar(50), TRAVEL_DATE date, TIME time)")
#print("TABLE CREATED SUCCESSFULLY")

#mycursor.execute("alter table bus add PRICE int")
#print("COLUMN ADDED SUCCESSFULLY")

#creating table car
#mycursor.execute("create table car(NAME varchar(50), AGE int, DESTINATION varchar(50), TRAVEL_DATE date, TIME time, PRICE int, MEMBERS int)")
#print("TABLE CREATED SUCCESSFULLY")

print("                                               WELCOME TO ROUTE ONLINE TICKING BOOKING")
print("IF YOU WANT TO SEE OUT POLICY PLEASE ENTER POLICY OR ELSE ENTER NO")

def POLICY():
    print("WE CAN AVAIL YOU CARS AND BUSES AND COMPARING TO OTHER TRAVEL AGENCY WE WILL GET LESS AMOUNT FROM YOU...WE WON'T APPLY ANY TAXES FOR YOU AFTER CANCELLING THE BOKKING...HAVE A HAPPY AND SAFER JOUNEY IF ANY QUERIES DURING TRAVEL YOU CALL CALL THE BELOW NUMBER (24/7)")
    print("9883447828")

def BUS():
    print("WELCOME HERE YOU CAN TRAVEL MAXIMUM OF 50 MEMBERS..IN BUS")
    print("PLACES PROVIDED ARE:")
    f = ["BANGALORE", "HYDRABAD", "DELHI", "AHMEDABAD", "ODISSA", "MAHARASHTRA", "KASHMIR", "GOA"]
    for i in f:
        print(i)
    d = int(input("HOW MANY OF YOU WANT TO TRAVEL:"))
    if d <= 50:
        e = str(input("PLEASE ENTER THE PLACE WHERE YOU WANNA GO:")).upper().strip()
        if e in f:
            if e == "BANGALORE":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.200 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*200)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-25', '12:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")
                    print(val)
                else:
                    print("THANK YOU")

            elif e == "HYDRABAD":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.400 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*400)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-23', '10:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")   

            elif e == "DELHI":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.700 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*700)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-30', '06:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "AHMEDAMAD":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.550 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*550)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-10-23', '10:00:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "ODISSA":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.900 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*900)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-11-23', '16:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "MAHARASHTRA":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.79 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*79)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-10-01', '23:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "KASHMIR":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.699 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*699)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-27', '01:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            else:
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.1500 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*1500)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into bus(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-11-18', '22:30:01', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")
        else:
            print("PLEASE SELECT FROM ABOVE LIST")          
    else:
        print("IN BUS WE CAN AVAIL YOU ONLY 50 AND IF YOU WANT MORE YOU CAN BOOK 2 BUSES")

def CAR():
    print("WELCOME HERE YOU CAN TRAVEL MAXIMUM OF 4 MEMBERS..IF YOU WANNNA TRAVEL WITH MORE THAN 4 YOU CAN TRY BUS")
    print("PLACES PROVIDED ARE:")
    f = ["BANGALORE", "HYDRABAD", "DELHI", "AHMEDABAD", "ODISSA", "MAHARASHTRA", "KASHMIR", "GOA"]
    for i in f:
        print(i)
    d = int(input("HOW MANY OF YOU WANT TO TRAVEL:"))
    if d <= 4:
        e = str(input("PLEASE ENTER THE PLACE WHERE YOU WANNA GO:")).upper().strip()
        if e in f:
            if e == "BANGALORE":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.500 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*500)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-25', '12:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")
                    print(val)
                else:
                    print("THANK YOU")

            elif e == "HYDRABAD":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.700 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*700)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-23', '10:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")   

            elif e == "DELHI":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.1000 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*1000)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-30', '06:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "AHMEDAMAD":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.850 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*850)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-10-23', '10:00:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "ODISSA":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.1200 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*1200)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-11-23', '16:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "MAHARASHTRA":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.379 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*379)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-10-01', '23:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            elif e == "KASHMIR":
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.999 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*999)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-09-27', '01:30:00', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")

            else:
                print(f"TICKETS FOR {e} IS AVAILABLE AND IT COSTS RS.2000 PER PERSON")
                print(f"SO THE COST FOR {d} PERSONS ARE:",d*2000)
                print("PLEASE FILL THE BELOW DETAILS TO BOOK YOUR SLOT:")
                g = str(input("NAME:")).upper().strip()
                h = int(input("AGE:"))
                i = int(input("PRICE DECLARED:"))  

                j = str(input("PLEASE CONFIRM YOUR SLOT BY TYPING OKAY.....")).lower().strip()
                if j == "okay":
                    sql = "insert into car(NAME, AGE, DESTINATION, TRAVEL_DATE, TIME, PRICE, MEMBERS) values(%s,%s,%s,%s,%s,%s,%s)"
                    val = (g, h, e, '2022-11-18', '22:30:01', i, d)
                    mycursor.execute(sql,val)
                    a.commit()
                    print("BOOKED")   
                    print(val)
                else:  
                    print("THANK YOU")
        else:
            print("PLEASE SELECT FROM ABOVE LIST")          
    else:
        BUS()

b = str(input("")).upper().strip()
if b == "POLICY":
    POLICY()
else:
    pass
    
print("WHAT TRAVEL YOU WANNA TAKE ENTER WHETHER 'CAR OR BUS'")
c = str(input("")).upper().strip()
if c == "CAR":
    CAR()
elif c == "BUS":
    BUS()
else:
    print("LOOKS YOU ARE SEARCHING FOR ANOTHER ONE WE CAN ONLY AVAIL YOU CARS AND BUSES WITH BETTER COMFORTABILITY")
