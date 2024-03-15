def doy():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select dayofyear(now())")
        dh=cur.fetchall()
        print(" ")
        print("displaying current day of year")
        print(" ")
        for jh in dh:
            for th in jh:
                print(th)
            print(" ")
    except c.Error as ter:
        print("something went wrong: {}".format(ter))
