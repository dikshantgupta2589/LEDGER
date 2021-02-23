import mysql.connector as sql
import datetime
import time
import getpass
def add():
    firm = input('ENTER THE NAME OF THE FIRM {table}:  ')
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='ledger')
    cursor = con.cursor()
    data =(( "create table %s"
    "(DATE date not null ,"
    "BILL_PAYMENT char(1) not null check(BILL_PAYMENT in ('BILL','PAYMENT')),"
    "AMOUNT int not null )") % (firm))
    cursor.execute(data)
    con.commit()
    con.close()
    return 'y'

def bill():
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='ledger')
    cursor = con.cursor()
    firm = input('ENTER THE FIRM NAME : ')
    cursor.execute("show tables")
    q = cursor.fetchall()
    for rows in q:
        if firm == rows[0]:
            year = int(input('ENTER THE YEAR OF BILLING :   '))
            month = int(input('ENTER THE MONTH OF BILLING :   '))
            date = int(input('ENTER THE DATE OF BILLING :   '))
            a = datetime.date(year,month,date)
            c = int(input('ENTER THE AMOUNT : '))
            d = "insert into {} values('{}','BILL',{})".format(firm,a,c)
            cursor.execute(d)
            con.commit()
            con.close()
            return 'y'
        else:
            print('FIRM NOT FOUND')
            con.close()
            return 'y'

def pay():
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='ledger')
    cursor = con.cursor()
    firm = input('ENTER THE FIRM NAME : ')
    cursor.execute("show tables")
    q = cursor.fetchall()
    for rows in q:
        if firm == rows[0]:
            year = int(input('ENTER THE YEAR OF PAYMENT :   '))
            month = int(input('ENTER THE MONTH OF PAYMENT :   '))
            date = int(input('ENTER THE DATE OF PAYMENT :   '))
            a = datetime.date(year,month,date)
            c = int(input('ENTER THE AMOUNT : '))
            cursor.execute("insert into {} values('{}','PAYMENT',{})".format(firm,a,c))
            con.commit()
            con.close()
            return 'y'
        else:
            print('FIRM NOT FOUND')
            con.close()
            return 'y'

def check(firm):
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='ledger')
    cursor = con.cursor()
    cursor.execute("show tables")
    q = cursor.fetchall()
    for rows in q:
        if firm == rows[0]:
            d = "select sum(AMOUNT) from {} group by BILL_PAYMENT having BILL_PAYMENT in ('BILL')".format(firm)
            cursor.execute(d)
            bill = cursor.fetchone()
            l = "select sum(AMOUNT) from {} group by BILL_PAYMENT having BILL_PAYMENT in ('PAYMENT')".format(firm)
            cursor.execute(l)
            payment = cursor.fetchone()
            if bill == None and payment == None:
                bal = 0
            elif bill == None and payment != None:
                bal = 0-payment[0]
            elif payment == None and bill != None:
                bal = bill[0]-0
            else:
                bal = (bill[0]-payment[0])
            if bal < 0:
                print('YOU HAVE GIVEN AN ADVANCE PAYMENT TO',firm,'OF Rs.',-bal)
                con.close()
                return 'y'
            else:
                print('YOUR BALANCE FOR',firm,'IS',bal)
                con.close()
                return 'y'
        else:
            print('FIRM NOT FOUND')
            con.close()
            return 'y'

def dele():
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='ledger')
    cursor = con.cursor()
    cursor.execute("show tables")
    q = cursor.fetchall()
    for i in range(cursor.rowcount):
        print(q[i][0])
    firm = input('ENTER THE FIRM NAME : ')
    for rows in q:
        if firm == rows[0]:
            d = "drop table {}".format(firm)
            cursor.execute(d)
            con.commit()
            con.close()
            return 'y'
        else:
            print('FIRM NOT FOUND')
            con.close()
            return 'y'
def ck():
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='ledger')
    cursor = con.cursor()
    cursor.execute("show tables")
    q = cursor.fetchall()
    if q == []:
        print('NO FIRM IS REGISTERED YET...!!!!!!')
        con.close()
        return
    else:
        for rows in q:
            n = cursor.rowcount
            print(n)
            for i in range(n):
                print(q[i][0])
            con.close()
            return

#main-------------------------------------------------------------------
print('\n\n\t\tWELCOME TO YOUR LEDGER DATABASE')
time.sleep(5)
while True:
    print('********************************************************************************************')
    ch = int(input('''1. ADD A FIRM
2. ADD A BILL TO A LEDGER ACCOUNT
3. ADD A PAYMENT TO A LENDER ACCOUNT
4. CHECK THE BALANCE
5. DELETE AN ACCOUNT
6. CHECK THE TOTAL FIRMS
7. EXIT

\tENTER YOUR CHOICE:  '''))
    if ch == 1:
        t = add()
        if t == 'y':
            pass
    elif ch == 2:
        t = bill()
        if t == 'y':
            pass
    elif ch == 3:
        t = pay()
        if t == 'y':
            pass
    elif ch == 4:
        firm = input('ENTER THE FIRM NAME : ')
        t = check(firm)
        if t == 'y':
            pass
    elif ch == 5:
        t = dele()
        if t == 'y':
            pass
    elif ch == 6:
        t = ck()
    elif ch == 7:
        break
    else:
        print('YOU HAVE ENTERED A WRONG CHOICE.......!!!!!!')
