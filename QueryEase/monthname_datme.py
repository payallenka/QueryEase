def mhe():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select monthname(now())")
        dg=cur.fetchall()
        print(" ")
        print("displaying current month name")
        print(" ")
        for jg in dg:
            for tg in jg:
                print(tg)
            print(" ")
    except  c.Error as dey:
        print("something went wrong: {}".format(dey))
