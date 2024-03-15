def dsc():
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
    print(" ")
    try:
        b=input("enter database for acessing the table ")
        bc="use {}".format(b)
        cur.execute(bc)
        print(" ")
        cur.execute("show tables;")
        print(" ")
        print("displaying existing tables")
        print(" ")
        qr=cur.fetchall()
        print(" ")
        for kl in qr:
            print(kl)
        print(" ")
        ds=input("enter table name ")
        df="desc {}".format(ds)
        cur.execute(df)
        tu=cur.fetchall()
        print(" ")
        for jk in tu:
            print(jk)
        print(" ")
    except c.Error as asz:
        print("something went wrong: {}".format(asz))
