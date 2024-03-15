def idx():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    cur.execute("show databases")
    fg = cur.fetchall()
    print(" ")
    for ui in fg:
        print(ui)
    print(" ")
    try:
        b=input("enter database for acessing the table ")
        bc="use {}".format(b)
        cur.execute(bc)
        print(" ")
        print("displaying existing tables")
        cur.execute("show tables")
        gh=cur.fetchall()
        print(" ")
        for vu in gh:
            print(vu)
        print(" ")
        ae = input("enter table name ")
        dn = "show index from {}".format(ae)
        cur.execute(dn)
        fg = cur.fetchall()
        for dm in fg :
            print(dm)
        print(" ")
    except c.Error as asd:
        print("something went wrong: {}".format(asd))
   
