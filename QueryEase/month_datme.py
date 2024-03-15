def mth():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select month(now())")
        dc=cur.fetchall()
        print(" ")
        print("displaying current month")
        print(" ")
        for jc in dc:
            for tc in jc:
                print(tc)
            print(" ")
    except c.Error as deh:
        print("something went wrong: {}".format(deh))
