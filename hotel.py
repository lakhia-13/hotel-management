import mysql.connector
import sys
mydb=mysql.connector.connect(host='localhost',user='root',passwd='your_password')
cursor=mydb.cursor()
cursor.execute('CREATE DATABASE if not exists hotel;')
sql="CREATE TABLE PINFO(pno int primary key,name varchar(20),roomno int(6),checkin varchar(20),checkout varchar(20);"
cursor.execute(sql)
print("Database Connection Sucessfully ")
patno = 0
num = 0


def add():
    global patno
    global num
    global cursor
    if patno<10:
        pno=int(input("Enter the customer's id: "))
        name=input('Enter the customer name: ')
        roomno=int(input("Enter the customer's room number: "))
        sql="INSERT INTO pinfo(pno,name,roomno,checkin,checkout) values (%s,%s,%s,%s,%s)"
        val=(pno,name,roomno)
        cursor.execute(sql,val)
        mydb.commit()
        #cursor.execute('COMMIT;')
        print("The data has been successfully added! \n")
        #cursor.execute('COMMIT;')
        patno = patno + 1
        Home()
    else:
        print("We are extremely sorry but we dont have any rooms")
    num = 10 -patno
    Home()


def see():
    id=int(input("Enter the customer's id whose information you want to see: "))
    print()
    cursor.execute('SELECT * from pinfo where pno= {};'.format(id,))
    data=cursor.fetchall()
    if len(data)==0:

        print("INCORRECT CUSTOMER ID \n")

    else:
        print("Customer id: ",data[0][0])
        print("Customer name: ",data[0][1])
        print("Customer room number: ",data[0][2])
        print()
        cursor.execute('COMMIT;')
        Home()
def update():
    id=int(input("Enter the customer's id whose data you want to update: "))
    name=input("Enter customer's new name :")
    room=int(input("Enter customer's new room number :"))
    sql="UPDATE PINFO SET name=%s ,roomno=%s where pno=%s"
    val=(name,room,id)
    cursor.execute(sql,val)
    print("Update successful! \n")
    cursor.execute('COMMIT;')
    Home()
def delete():
    global patno
    global num
    id=int(input("Enter the customer's id whose data you want to delete: "))
    cursor.execute('DELETE from pinfo where pno= {};'.format(id,))
    cursor.execute('COMMIT;')
    print("Info Deleted")
    patno = patno -1
    num = 10 -patno
    Home()
def check():
    print("We have a capacity of 10 rooms and we have",num, "rooms vacant")
    Home()

def passmanagement():
    print('****************************************************WELCOME TO HOTEL MANAGEMNET SOFTWARE*********************************************************************')
    x = int(input("Only authorised personnel can access patient's information enter 1 to access"))
    if x == 1:
        while True:
            user=input("Enter your user id: ")
            psw=input("Enter your password: ")
            if user=='admin' and psw=='Admin123':
                print('Access granted! \n')
                Home()
                break
            else:
                print("Incorrect user id or password. Please try again.")
def Home():
    print('MENU \n')
    print('1) Add new data')
    print('2) Customer info')
    print('3) Delete data')
    print('4) Update data')
    print('5) Check rooms')
    print('6) Exit')

    choice=int(input("Enter your choice: "))
    if choice==1:
        add()
    elif choice==2:
        see()
    elif choice==3:
        delete()
    elif choice==4:
        update()
    elif choice==5:
        check()
    elif choice==6:
         print("Thank you for using Hotel Management Software")
         print("Have a great day")
         sys.exit()
    else:
         print("Please enter a valid input")

passmanagement()
