def dte():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select curdate()")
        da=cur.fetchall()
        print(" ")
        print("displaying current time")
        print(" ")
        for ja in da:
            for ta in ja:
                print(ta)
            print(" ")
    except c.Error as des:
        print("something went wrong: {}".format(des))
    
