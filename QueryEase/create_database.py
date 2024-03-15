def credat():
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
    print(" ")
    print("preferably enter name with '_'(underscore) for smooth functioning")
    print(" ")
    try:
        b=input("enter the name of your new database ")
        be="create database {};".format(b)
        cur.execute(be)
        print("database created")
        print(" ")
        cur.execute("show databases;")
        l=cur.fetchall()
        for i in l:
            print(i)
        print(" ")
    except c.Error as aso:
        print("something went wrong: {}".format(aso))
