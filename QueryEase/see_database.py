def sedat():
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
    print()
    print("displaying existing databases")
    print()
    for i in l:
        print(i)
    print()
