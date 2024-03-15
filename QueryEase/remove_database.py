def redat():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    cur.execute("show databases;")
    l1=cur.fetchall()
    print()
    for i in range(0,len(l1)):
        print(l1[i])
    print()
    try:
        b=input("enter the name of the database you want to remove ")
        q="drop database {}".format(b)
        cur.execute(q)
        print(" ")
        print("database removed")
        print(" ")
        cur.execute("show databases;")
        l=cur.fetchall()
        for r in l:
            print(r)
    except c.Error as aqw:
        print("something went wrong: {}".format(aqw))
