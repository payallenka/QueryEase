def udte():
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
        print(" ")
        for kl in qr:
            print(kl)
        print(" ")
        s=input("enter table name you want to update ")
        print(" ")
        print("description of table")
        bdc = "desc {}".format(s)
        cur.execute(bdc)
        l=cur.fetchall()
        print(" ")
        for i in l:
            print(i)
        print(" ")
        bc = "select * from {}".format(s)
        cur.execute(bc)
        lz=cur.fetchall()
        print(" ")
        for ix in lz:
            print(ix)
        print(" ")
        t=input("enter the condition using the syntax - column_name_to_be_updated = updated_record where = condition_ ")
        st="update {} set {};".format(s,t)
        cur.execute(st)
        con.commit()
        ge="select * from {}".format(s)
        cur.execute(ge)
        l3=cur.fetchall()
        print(" ")
        print("modified table values")
        print(" ")
        for jj in l3:
            print(jj)
        print(" ")
    except c.Error as asi:
        print("something went wrong: {}".format(asi))