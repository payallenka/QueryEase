def ist():
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
     try:
          b=input("enter database for acessing the table ")
          bc="use {}".format(b)
          cur.execute(bc)
          print(" ")
          cur.execute("show tables;")
          print(" ")
          print("displaying existing tables")
          print(" ")
          qr=cur.fetchall()
          print(" ")
          if len(qr)==0:
               print()
               print("no pre-existing tables present")
               print("you need to create a table and then you can use the insert feature")
               print("for that you need to use the 'create' feature")
               print()
               
          else:
               for kl in qr:
                    print(kl)
               print(" ")
               y=input("enter table name in which you want to insert values ")
               r=int(input("how many values you want to insert "))
               num=0
               bdc = "desc {}".format(y)
               cur.execute(bdc)
               l2=cur.fetchall()
               print(" ")
               for ii in l2:
                    print(ii)
               print(" ")
               yr="select * from {};".format(y)
               cur.execute(yr)
               ro=cur.fetchall()
               print(" ")
               print("displaying existing records in the table")
               for u in ro:
                    print(u)
               print(" ")
               while num<r:
                    print(" ")
                    print("if the input is in char or varchar format then enclose that value in '_'")
                    print(" ")
                    print(" ")
                    print("if you want to enter values in specific columns then mention the column names below")
                    try:
                         xb = input("enter specific columns; else just press enter ")
                         print()
                         print("enter values for varchar and char enclosed in 'inverted commas' ")
                         print()
                         f= input("enter your values in the sequence of your column: ")
                         ye= "insert into {}({}) values({});".format(y,xb,f)
                         cur.execute(ye)
                         con.commit()
                         num+=1
                    except c.Error as asi:
                         print("something went wrong: ()".format(asi))
     except c.Error as asl:
          print("something went wrong: {}".format(asl))
    
