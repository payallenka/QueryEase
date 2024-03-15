def scd():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select second(now())")
        de=cur.fetchall()
        print(" ")
        print("displaying current second")
        print(" ")
        for je in de:
            for te in je:
                print(te)
            print(" ")
    except c.Error as deo:
        print("something went wrong: {}".format(deo))
