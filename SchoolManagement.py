# Main Program
import mysql.connector as a
con = a.connect(host='localhost', user='root', passwd='root', database='school')

def addst():
    n = input("Student name : ")
    cl = input("Class : ")
    r = int(input("Roll no. : "))
    a = input("Address : ")
    ph = int(input("Phone no. : "))
    data = (n, cl, r, a, ph)
    sql = 'insert into student values (%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    print("")

def removest():
    cl = input("class : ")
    r = input("roll no. : ")
    data = (cl, r)
    sql = 'delete from student where class=%s and roll=%s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data deleted successfully")
    print("")

def displayst():
    cl = input("class : ")
    data = (cl,)
    sql = 'select * from student where class=%s'
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print("Name : ", i[0])
        print("class : ", i[1])
        print("roll no. : ", i[2])
        print("address : ", i[3])
        print("phone no. : ", i[4])
        print("")
    print("")

def addt():
    tid = int(input("teacher ID : "))
    n = input("Name : ")
    s = int(input("Salary : "))
    a = input("Address : ")
    ph = int(input("Phone no. : "))
    data = (tid, n, s, a, ph)
    sql = 'insert into teacher values (%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    print("")

def removet():
    n = input("Teacher name : ")
    tid = int(input("teacher ID : "))
    data = (n, tid)
    sql = 'delete from teacher where name=%s and id=%s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data deleted successfully")
    print("")

def updatesal():
    n = input("Name : ")
    tid = int(input("teacher ID : "))
    s = int(input("Salary : "))
    data = (s, n, tid)
    sql = 'update teacher set salary=%s where name=%s and id=%s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("salary updated successfully")
    print("")

def displayt():
    sql = 'select * from teacher'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("teacher ID: ", i[0])
        print("name : ", i[1])
        print("salary : ", i[2])
        print("address : ", i[3])
        print("phone no. : ", i[4])
        print("")
    print("")

def clattd():
    d = input("class : ")
    clt = input("Class teacher : ")
    t = int(input("Class strength : "))
    d = input("date : ")
    ab = int(input("No. of absentees : "))
    data = (d, clt, t, ab)
    sql = 'insert into ClAttendance values (%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    print("")

def displayclattd():
    sql = 'select * from CLAttendance'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("class : ", i[0])
        print("class teacher : ", i[1])
        print("total student : ", i[2])
        print("date : ", i[3])
        print("absentees : ", i[4])
        print("")
    print("")

def tattd():
    d = input("date : ")
    t = input("total teacher : ")
    ta = input("no. of teacher absent : ")
    data = (d, t, ta)
    sql = 'insert into tattendance values (%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    print("")

def displaytattd():
    sql = 'select * from tattendance'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("date : ", i[0])
        print("total teachers : ", i[1])
        print("no. of teacher absent : ", i[2])
        print("")
    print("")

def updatefees():
    cl = input("class : ")
    m = input("monthly : ")
    b = input("Busfee : ")
    sc = input("scfee : ")
    tc = input("techfee : ")
    t = input("total : ")
    data = (cl, m, b, sc, tc, t)
    sql = 'insert into Feestructure values (%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data updated successfully")
    print("")

def displayfees():
    sql = 'select * from Feestructure'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("class : ", i[0])
        print("monthly : ", i[1])
        print("busfee : ", i[2])
        print("scfee: ", i[3])
        print("techfee : ", i[4])
        print("total : ", i[5])
        print("")
    print("")

def addbook():
    bid = input("Book ID : ")
    t = input("Title: ")
    a = input("Author : ")
    p = input("Publisher : ")
    g = input("Genre : ")
    data = (bid, t, a, p, g)
    sql = 'insert into library values (%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("data entered successfully")
    print("")

def removeb():
    title = input("title: ")
    id = int(input("book id : "))
    data = (title, id)
    sql = 'delete from library where title=%s and id=%s'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Book deleted successfully")
    print("")

def displayb():
    sql = 'select * from library'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("book id : ", i[0])
        print("title : ", i[1])
        print("author : ", i[2])
        print("publisher : ", i[3])
        print("genre : ", i[4])
        print("")
    print("")

def main():
    ch = 'y'
    while ch in ['y', 'Y']:
        print("SCHOOL MANAGEMENT SYSTEM")
        print(''' 1. student
2. teacher
3. CLAttendance
4. TAttendance
5. fee structure
6. library''')
        table = int(input("enter table no. : "))
        print("")
        if table == 1:
            op = 'y'
            while op in ['y', 'Y']:
                print(''' 1. add student
2. delete student
3. display student detail ''')
                task = int(input("enter task no. : "))
                if task == 1:
                    addst()
                elif task == 2:
                    removest()
                elif task == 3:
                    displayst()
                else:
                    print("enter valid choice ")
                op = input("continue in this table (y/n): ")
        elif table == 2:
            op = 'y'
            while op in ['y', 'Y']:
                print(''' 1. add teacher
2. remove teacher
3. update salary
4. display teacher detail''')
                task = int(input("enter task no. : "))
                if task == 1:
                    addt()
                elif task == 2:
                    removet()
                elif task == 3:
                    updatesal()
                elif task == 4:
                    displayt()
                else:
                    print("enter valid choice ")
                op = input("continue in this table (y/n): ")
        elif table == 3:
            op = 'y'
            while op in ['y', 'Y']:
                print(''' 1. class attendance
2. display class attendance detail''')
                task = int(input("enter task no. : "))
                if task == 1:
                    clattd()
                elif task == 2:
                    displayclattd()
                else:
                    print("enter valid choice ")
                op = input("continue in this table (y/n): ")
        elif table == 4:
            op = 'y'
            while op in ['y', 'Y']:
                print(''' 1. teacher attendance
2. display teacher attendance detail''')
                task = int(input("enter task no. : "))
                if task == 1:
                    tattd()
                elif task == 2:
                    displaytattd()
                else:
                    print("enter valid choice ")
                op = input("continue in this table (y/n): ")
        elif table == 5:
            op = 'y'
            while op in ['y', 'Y']:
                print(''' 1. update fees
2. display fees detail''')
                task = int(input("enter task no. : "))
                if task == 1:
                    updatefees()
                elif task == 2:
                    displayfees()
                else:
                    print("enter valid choice ")
                op = input("continue in this table (y/n): ")
        elif table == 6:
            op = 'y'
            while op in ['y', 'Y']:
                print(''' 1. add book
2. remove book
3. display book ''')
                task = int(input("enter task no. : "))
                if task == 1:
                    addbook()
                elif task == 2:
                    removeb()
                elif task == 3:
                    displayb()
                else:
                    print("enter valid choice ")
                op = input("continue in this table (y/n): ")
        else:
            print("enter valid choice ")
        ch = input("do you want to continue (y/n):")
            
main()