def tey():
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
        print(" ")
        print("displaying existing tables")
        print(" ")
        qr=cur.fetchall()
        print(" ")
        for kl in qr:
            print(kl)
        print(" ")
        rt = input("enter table name ")
        tr = "show create table {}".format(rt)
        cur.execute(tr)
        pr = cur.fetchall()
        print(" ")
        for lm in pr:
            for ti in lm:
                print(ti)
            print(" ")
    except c.Error as asf:
        print("something went wrong: {}".format(asf))
