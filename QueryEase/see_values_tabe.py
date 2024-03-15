def slu():
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
        try:
            b=input("enter database for acessing the table ")
        except:
            print("invalid input")
            
        bc="use {}".format(b)
        cur.execute(bc)
        print(" ")
        cur.execute("show tables;")
        x=cur.fetchall()
        print(" ")
        print("displayig existing tables")
        if len(x)==0:
            print(" ")
            print("no values inserted")
            print(" ")       
        else:
            print(" ")
            for i in x:
                print(i)
            print(" ")
            try:
                ji = input("enter table name to see its values ")
                print("invalid input")
                fg = "select * from {};".format(ji)
                cur.execute(fg)
                lo = cur.fetchall()
                print()
                print("displaying existing values")
                print()
                if len(lo)==0:
                    print()
                    print("no existing values in the table")
                    print()
                else:
                    for ui in lo:
                        print(ui)
            except c.Error as igi:
                print("something went wrong: {}".format())
    except c.Error as fgt:
        print("something went wrong: {}".format(fgt))
