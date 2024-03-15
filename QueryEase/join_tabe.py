def jin():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    cur.execute("show databases;")
    l=cur.fetchall()
    for i in l:
        print(i)
    print(" ")
    try:
        b=input("enter database for acessing the table ")
        bc="use {}".format(b)
        cur.execute(bc)
        print(" ")
        cur.execute("show tables;")
        qr=cur.fetchall()
        if len(qr)<=1:
            print(" ")
            print("for using the 'join' feature atleast two tables are required")
            print("kindly create another table to use this feature")
            print("this can be done using 'create' feature")
            print(" ")
            
        else:
            try:
                print(" ")
                for kl in qr:
                    print(kl)
                print(" ")
                s= input("enter table name 1 ")
                t= input("enter table name 2 ")
                print(" ")
                print(" describstion of table: ",s)
                bdc = "desc {}".format(s)
                cur.execute(bdc)
                l=cur.fetchall()
                print(" ")
                for i in l:
                    print(i)
                print(" ")
                print(" describtion of table: ",t)
                bd = "desc {}".format(t)
                cur.execute(bd)
                l2=cur.fetchall()
                print(" ")
                for ii in l2:
                    print(ii)
                print(" ")
                print("with respect to table_1 and table_2")
                u= input("enter column names that you wish to join seperated by ',' ")
                v=input("enter column name 1 that is common corresponding to table 1 ")
                w= input("enter column name 2 that is common corresponding to table2 ")
                stu="select {} from {},{} where {}={} ; ".format(u,s,t,v,w)
                cur.execute(stu)
                yu=cur.fetchall()
                print(" ")
                for ru in yu:
                    print(ru)
                print(" ")
            except c.error as asdf:
                print("something went wrong: {}").format(asdf)
    except c.Error as ast:
        print("something went wrong: {}".format(ast))
