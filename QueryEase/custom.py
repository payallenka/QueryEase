def cus():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        uio = input("enter a query ")
        cur.execute(uio)
        con.commit()
    except c.Error as dft:
        print("something went wrong: {}".format(dft))
