import mysql.connector as sql

print("First you connect with database than do what you want to do.")
host = input("Enter your host name: ")
user = input("Enter your user name: ")
password = input("Enter your mysql password: ")
while True:
    dataBase = ['1.mydb', '2.library', '3.addmin']
    for base in dataBase:
        print(base)
    databases = input("Enter database which you want to connect: ")

    con = sql.connect(host=host, user=user, passwd=password, database=databases)
    # con = sql.connect(host="localhost", user="root", passwd="satyam", database="addmin")
    # For database mydb

    if con.is_connected() == True:
        if databases == "mydb":
            print("Connection Successfully set-up")
            cur = con.cursor()
            while True:
                print("Select which table you want to access: ")
                listOfTable = ["1.EMP", "2.STUDENT"]
                for name in listOfTable:
                    print(name)
                tableName = input("Enter table name: ")
                print("==============Welcome to MyDatabase==============")
                print('''
                Please choose correct option:
                    1.Display all records.
                    2.Insert records.
                    3.Update records.
                    4.Delete records.
                    5.Search records.
                    6.Exit.
                ''')
                choice = int(input("Enter your choice 1 to 6: "))
                if choice == 1:
                    # Display all records.

                    cur.execute(f"select * from {tableName}")
                    data = cur.fetchall()
                    for row in data:
                        print(row)

                elif choice == 2:
                    # Insert records into the tables.

                    if tableName == "emp":
                        # for emp table.
                        commTake = input("Employee take commission? If yes type 'y' else no type 'n': ")
                        if commTake == 'n' or commTake == 'n':
                            empno = input("Enter employee number: ")
                            ename = input("Enter employee name: ")
                            job = input("Enter employee job: ")
                            gender = input("Enter employee gender: ")
                            sal = input("Enter salary of the employee:")
                            deptno = input("Enter department number: ")
                            value = "insert into emp (empno,ename,job,gender,sal,deptno) VALUES ({}, '{}', '{}', '{}', {} ,{})".format(
                                empno, ename, job, gender, sal, deptno)
                            cur.execute(value)
                            print("Your records is successfully inserted.....")
                            con.commit()
                        elif (commTake == 'y' or commTake == 'Y'):
                            empno = input("Enter employee number: ")
                            ename = input("Enter employee name: ")
                            job = input("Enter employee job: ")
                            gender = input("Enter employee gender: ")
                            sal = input("Enter salary of the employee: ")
                            comm = input("Enter comission of the employee: ")
                            deptno = input("Enter department number: ")
                            value = "insert into emp (empno,ename,job,gender,sal,comm,deptno) VALUES ({},'{}','{}','{}',{},{},{})".format(
                                empno, ename, job, gender, sal, comm, deptno)
                            cur.execute(value)
                            print("Your records is successfully inserted.....")
                            con.commit()
                        else:
                            print("Invalid Input!!!")

                    elif tableName == "student":
                        # for student table.
                        roll = input("Enter roll number of the student: ")
                        name = input("Enter name of the student: ")
                        std = input("Enter standered of the student: ")
                        sec = input("Enter section of the student: ")
                        city = input("Enter city of the student: ")
                        values = "insert into student values ({}, '{}', '{}', '{}','{}')".format(roll, name, std, sec,
                                                                                                 city)
                        cur.execute(values)
                        print("Your records is successfully inserted.....")
                        con.commit()

                elif choice == 3:
                    # Updating the tables
                    if tableName == "emp":
                        print('''
                            1.Salary.
                            2.Commination.
                            3.Department Number.
                            4.Name.
                        ''')

                        updateChoice = int(input("What you want to update. Choose correct option: "))

                        if updateChoice == 1:
                            newSal = input("Enter updated salary of the employee: ")
                            empNo = input("Enter employee id to update their salary: ")
                            cur.execute("update emp set sal = {} where empno = {}".format(newSal, empNo))
                            print("Your records is updated.....")
                            con.commit()

                        elif updateChoice == 2:
                            newComm = input("Enter updated commination of the employee: ")
                            empNo = input("Enter employee id to update their commination: ")
                            cur.execute("update emp set comm = {} where empno = {}".format(newComm, empNo))
                            print("Your records is updated......")
                            con.commit()

                        elif updateChoice == 3:
                            newDept = input("Enter updated department number of the employee: ")
                            empNo = input("Enter employee id to update their department number: ")
                            cur.execute("update emp set deptno = {} where empno = {}".format(newDept, empNo))
                            print("Your records is updated......")
                            con.commit()

                        elif updateChoice == 4:
                            newEname = input("Enter updated name of the employee: ")
                            empNo = input("Enter employee id to update their name: ")
                            cur.execute("update emp set ename = '{}' where empno = {}".format(newEname, empNo))
                            print("Your records is updated......")
                            con.commit()

                        else:
                            print("Please enter correct option.")

                    elif tableName == "student":
                        print('''
                            1.City.
                            2.Marks.
                            3.Name.
                            4.Class
                        ''')

                        updateOption = int(input("What you want to update. Choose correct option: "))

                        if updateOption == 1:
                            newCity = input("Enter new city of the student: ")
                            roll = input("Enter roll number of the student to update their city: ")
                            cur.execute("update student set city = '{}' where roll = {}".format(newCity, roll))
                            print("Your records is updated.....")
                            con.commit()

                        elif updateOption == 2:
                            newMarks = input("Enter new marks of the student: ")
                            roll = input("Enter roll number of the student to update their marks: ")
                            cur.execute("update student set marks = {} where roll = {}".format(newMarks, roll))
                            print("Your records is updated.....")
                            con.commit()

                        elif updateOption == 3:
                            newName = input("Enter updated name of the student: ")
                            roll = input("Enter roll number of the studnet to update their name: ")
                            cur.execute("update student set name = '{}' where roll = {}".format(newName, roll))
                            print("Your records is successfully updated.....")
                            con.commit()

                        elif updateOption == 4:
                            newClass = input("Enter updated class of the student: ")
                            roll = input("Enter roll number of the student to update their class: ")
                            cur.execute("update student set class = '{}' where roll = {}".format(newClass, roll))
                            print("Your records is successfully updated.....")
                            con.commit()

                        else:
                            print("Please choose correct option.")

                elif choice == 4:
                    # Delete records from the tables.

                    if tableName == "emp":
                        emp = input("Enter employee id: ")
                        deleteId = "delete from emp where empno = {}".format(emp)
                        cur.execute(deleteId)
                        print("Your records is successfully deleted.....")
                        con.commit()
                    elif tableName == "student":
                        roll = input("Enter student roll number: ")
                        deleteRoll = "delete from student where roll = {}".format(roll)
                        cur.execute(deleteRoll)
                        print("Your records is successfully deleted.....")
                        con.commit()

                    # Search records from the tables.
                elif choice == 5:

                    # search coding for emp table.

                    if tableName == "emp":
                        print("In which bases you want to search the records. Please choose the correct option: ")
                        print('''
                                1.On the bases of empno.
                                2.On the bases of name.
                                3.Check the commination is NULL.
                                4.Check the commination is not NULL.
                                ''')
                        choose = int(input("Enter your choice 1-3: "))
                        if choose == 1:
                            empId = input("Enter employee id: ")
                            try:
                                cur.execute("select * from emp where empno = {}".format(empId))
                                empnoList = []
                                data = cur.fetchone()
                                for emp in data:
                                    empnoList.append(emp)
                                print(empnoList)
                            except:
                                print("No data found.....")

                        elif choose == 2:
                            name = input("Enter name of the employee: ")
                            try:
                                cur.execute("select * from emp where ename = '{}'".format(name))
                                enameList = []
                                val = cur.fetchone()
                                for ename in val:
                                    enameList.append(ename)
                                print(enameList)
                            except:
                                print("No data found.....")

                        elif choose == 3:
                            cur.execute("select * from emp where comm IS NULL")
                            data = cur.fetchall()
                            for row in data:
                                print(row)

                        elif choose == 4:
                            cur.execute("select * from emp where comm IS NOT NULL")
                            data = cur.fetchall()
                            for row in data:
                                print(row)

                        else:
                            print("Please choose correct option.....")

                    # search coding for student table.

                    elif tableName == "student":

                        print("In which bases you want to search the records. Please choose the correct option: ")
                        print('''
                            1.On the bases of roll no.
                            2.On the bases of name.
                            ''')
                        option = int(input("Enter your option 1-2: "))
                        if option == 1:
                            studentRoll = int(
                                input("Enter roll number of the student: "))
                            try:
                                cur.execute("select * from student where roll = {}".format(studentRoll))
                                rollList = []
                                roll = cur.fetchone()
                                for one in roll:
                                    rollList.append(one)
                                print(rollList)
                            except:
                                print("No data found")

                        elif option == 2:
                            studentName = input("Enter name of the student: ")
                            try:
                                cur.execute("select * from student where name = '{}'".format(studentName))
                                nameList = []
                                rec = cur.fetchone()
                                for sname in rec:
                                    nameList.append(sname)
                                print(nameList)
                            except:
                                print("No data found")

                        else:
                            print("Choose correct option.")

                elif choice == 6:
                    print("Thank You!!!")
                    break
                cont = input(f"Do you want to continue with {databases}? If yes type 'Y' else type 'N' : ")
                if cont == 'Y' or cont == 'y':
                    continue
                else:
                    print("Thank You for using this app.")
                    break

        # for database library
        elif databases == "library":
            while (True):
                curr = con.cursor()
                print("======Welcome to KVS Library======")
                menu = '''
                    Please select correct option for go ahead:
                        1.Display all books.
                        2.Issue/Request books.
                        3.Return Books.
                        4.Exit
                    '''
                print(menu)
                choose = int(input("Enter your choice from 1-4: "))
                if choose == 1:
                    curr.execute(f"select * from book")
                    rec = curr.fetchall()
                    for records in rec:
                        print(records)

                elif choose == 2:
                    bookName = input("Enter book name which you want to issue: ")
                    dele = "delete from book where book_name = '{}'".format(
                        bookName)
                    curr.execute(dele)
                    print(f"{bookName} is issue to you.")
                    con.commit()

                elif choose == 3:
                    book_id = input("Enter Book id: ")
                    bookName = input("Enter book name: ")
                    authorName = input("Enter author name: ")
                    publish = input("Enter publisher name: ")
                    price = input("Enter book price: ")
                    type_ = input("Enter type of the book: ")
                    value = "insert into book VALUES ({},'{}','{}','{}',{},'{}')".format(book_id, bookName, authorName,
                                                                                         publish, price, type_)
                    curr.execute(value)
                    print("You have return the book which you have issue now you have issue any book to the library.")
                    con.commit()
                elif choose == 4:
                    print("Thank you for visiting our library.")
                    break
                cont = input(f"Do you wnat to continue with {databases}? If yes type 'Y' else type 'N' : ")
                if (cont == 'Y' or cont == 'y'):
                    continue
                else:
                    print("Thank You for using this app.")
                    break

        elif (databases == "addmin"):
            while True:
                cur = con.cursor()
                print('''======Welcome to KVS=======''')
                print('''
                Please choose correct option for do your opration smoothly: 
                    1.Display all records.
                    2.Take addmination in KVS.
                    3.Take TC from KV.
                ''')
                choice = int(input("Choose your option (1-3): "))
                if choice == 1:
                    cur.execute("select * from school")
                    for row in cur:
                        print(row)

                elif choice == 2:
                    addno = input("Enter addmination number of the student: ")
                    roll = input("Enter roll number of the student: ")
                    name = input("Enter name of the student: ")
                    value = "insert into school Values ({}, {}, '{}')".format(addno, roll, name)
                    cur.execute(value)
                    print(f"{name} is addmitied in KVS. Welcome to KVS.....")
                    con.commit()

                elif choice == 3:
                    addno = input("Enter addmination number of the student: ")
                    delete = "delete from school where addmno = {}".format(addno)
                    cur.execute(delete)
                    print("You get successfully T.C. from KVS.")
                    con.commit()

                else:
                    print("Please choose correct option!!!\nInvalid Option!!!!")

                cont = input(f"Do you want to continue with {databases}? If yes type 'Y' else type 'N' : ")
                if cont == 'Y' or cont == 'y':
                    continue
                else:
                    print("Thank You for using this app.")
                    break
    else:
        print("Connection unsuccessful")

    con.close()
    cont = input("Do you want to continue with this app? If yes type 'Y' else type 'N' : ")
    if cont == 'Y' or cont == 'y':
        continue
    else:
        print("Thank You for using this app.")
        break
