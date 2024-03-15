def cal():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        qw= input("enter numerical ")
        df = "select {}".format(qw)
        cur.execute(df)
        dh = cur.fetchall()
        for u in dh:
            for y in u:
                print("Ans : ",y)
    except c.Error as defe:
        print("something went wrong: {}".format(defe))
