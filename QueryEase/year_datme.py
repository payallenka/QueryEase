def yer():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select year(now())")
        db=cur.fetchall()
        print(" ")
        print("displaying current time")
        print(" ")
        for jb in db:
            for tb in jb:
                print(tb)
        print(" ")
    except c.Error as deg:
         print("something went wrong: {}".format(deg))
