def tme():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select curtime()")
        ds=cur.fetchall()
        print(" ")
        print("displaying current time")
        print(" ")
        for jk in ds:
            for tu in jk:
                print(tu)
            print(" ")
    except c.Error as dea:
        print("something went wrong: {}".format(dea))
