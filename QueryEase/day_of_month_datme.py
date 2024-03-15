def dom():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select dayofmonth(now())")
        di=cur.fetchall()
        print(" ")
        print("displaying current day of month")
        print(" ")
        for ji in di:
            for ti in ji:
                print(ti)
            print(" ")
    except c.Error as det:
        print("something went wrong: {}".format(det))
