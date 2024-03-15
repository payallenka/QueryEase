def cet():
    f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","r")
    a=f.readline()
    b=f.readline()
    gh=f.readline()
    f.close()
    import mysql.connector as c
    con=c.connect(host=a,user=b,password=gh)
    cur=con.cursor()
    try:
        cur.execute("show databases;")
        l=cur.fetchall()
        for i in l:
            print(i)
        print(" ")
        b=input("enter database for acessing the table ")
        bc="use {}".format(b)
        cur.execute(bc)
        cur.execute("show tables;")
        go=cur.fetchall()
        if len(go)==0:
            print("empty database - no tables")
            print(" ")
        else:
            print(" ")
        print("displaying existing tables")
        for hu in go:
            print(hu)
        print(" ")
        print(" ")
        print("preferably enter column name with '_'(underscore) for smooth functioning")
        print(" ")
        c=input("enter the name of the table you want to create ")
        print(" ")
        print("preferably enter column name with '_'(underscore) for smooth functioning")
        print(" ")
        d=input("enter the column names and citeria of the table seperated by ','(comma) ")
        try:
            deli ="create table {}({})".format(c,d)
            cur.execute(deli)
            print(deli)
            bdc = "desc {}".format(c)
            cur.execute(bdc)
            l=cur.fetchall()
            print(" ")
            for i in l:
                print(i)
            print(" ")
            e= input("do you want to insert values(y/n): ") #insert values in table
            if e=="y":
                print(" ")
                g=int(input("how many values do you want to insert "))
                num = 0
                while num<g:             #reveiw for this loop has to be taken from ma'am
                    print(" ")
                    print("if the input is in char or varchar format then enclose that value in ' '(inverted commas)")
                    print(" ")
                    print("if you want to enter values in specific columns then mention the column names below")
                    xb = input("enter specific columns; else just press enter ")
                    f= input("enter your values in the sequence of your column: ")
                    try:
                        fg = "insert into {} ({}) values({});".format(c,xb,f)
                        cur.execute(fg)
                        con.commit()
                        num+=1
                    except c.Error as den:
                        print("something went wrong {}:".format(den))
        except c.Error as delop:
            print("something went wrong: {}".format(delop))
    except c.Error as deliver:
        print("something went wrong: {}".format(deliver))
