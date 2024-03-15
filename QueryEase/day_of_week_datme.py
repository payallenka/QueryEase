def dow():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select dayofweek(now())")
        dj=cur.fetchall()
        print(" ")
        print("displaying current day of week")
        print(" ")
        for jj in dj:
            for tj in jj:
                print(tj)
            print(" ")
    except c.Error as der:
        print("something went wrong: {}".format(der))
