def datsyn():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("show databases")
        fg = cur.fetchall()
        print(" ")
        for ui in fg:
            print(ui)
        print(" ")
        po = input("enter database name to see its syntax ")
        rp = "show create database {}".format(po)
        cur.execute(rp)
        dw = cur.fetchall()
        print(" ")
        for gz in dw:
            for qm in gz:
                    print(qm)
            print(" ")
    except c.Error as daf:
        print("something went wrong: {}".format(daf))
