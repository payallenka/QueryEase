def dye():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("select dayname(now())")
        df=cur.fetchall()
        print(" ")
        print("displaying current day name")
        print(" ")
        for jf in df:
            for tf in jf:
                print(tf)
            print(" ")
    except c.Error as deu:
        print("something went wrong: {}".format(deu))
