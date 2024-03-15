def hur():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select hour(now())")
        dd=cur.fetchall()
        print(" ")
        print("displaying current hour")
        print(" ")
        for jd in dd:
            for td in jd:
                print(td)
            print(" ")
    except c.Error as dep:
        print("something went wrong: {}".format(dep))
    
