def sele():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    cur.execute("show databases;")
    l=cur.fetchall()
    for i in l:
        print(i)
    print(" ")
    b=input("enter database for acessing the table ")
    bc="use {}".format(b)
    cur.execute(bc)
    print(" ")
    print("displaying existing tables")
    cur.execute("show tables")
    gh=cur.fetchall()
    if len(gh)==0:
        print("empty database - has no tables")
        print()
    else:
        print(" ")
        for vu in gh:
            print(vu)
    print(" ")
