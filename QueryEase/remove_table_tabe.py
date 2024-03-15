def rove():
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
        g= input("enter table name ")
        ge= "drop table {}".format(g)
        cur.execute(ge)
        cur.execute("show tables")
        l=cur.fetchall()
        for i in l:
            print(i)
    except c.Error as asy:
        print("something went wrong: {}".format(asy))
