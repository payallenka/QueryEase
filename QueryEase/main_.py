def pyql():
    try:
        import mysql.connector as c
        a=input("enter host name ")
        b=input("enter user name ")
        d=input("enter password of the database ")
        con=c.connect(host= a,user= b,password=d)
        cur=con.cursor()
        f=open("C:\\Users\\PAYAL-PIU\\AppData\\Local\\Programs\\Python\\Python39\\pyql\\details_.txt","w")
        lif=[a,"\n",b,"\n",d]
        for i in lif:
            f.write(i)
        #print("data written")
        f.close()
        print("connection established")
        print()
        value = -1
        
    except c.Error as e:
        value = 78
        print("something went wrong: {}".format(e))
    val = value   
    while val==-1:
        from menu import meu
        meu()
        ask=input("what do you want to do? ")
        print()
        if ask=="see database":
            from see_database import sedat
            sedat()
        elif ask=="create database":
            from create_database import credat
            credat()
        elif ask=="remove database":
            from remove_database import redat
            redat()
        elif ask=="custom":
            from custom import cus
            cus()
        elif ask=="database syntax":
            from database_syntax import datsyn
            datsyn()
        elif ask=="exit":
            con.close()
            print("bye")
            val=34
        elif ask=="calc":
            from calc import cal
            cal()
        elif ask=="datetime":
            from menu_datme import mnu
            mnu()
            qry=input("what do you want to see ")
            if qry=="time":
                from time_datme import tme
                tme()
            elif qry=="date":
                from date_datme import dte
                dte()
            elif qry=="hour":
                from hour_datme import hur
                hur()
            elif qry=="month":
                from month_datme import mth
                mth()
            elif qry=="year":
                from year_datme import yer
                yer()
            elif qry=="minute":
                from minute_datme import mtu
                mtu()
            elif qry=="second":
                from second_datme import scd
                scd()
            elif qry=="dayname":
                from dayname_datme import dye
                dye()
            elif qry=="monthname":
                from monthname_datme import mhe
                mhe()
            elif qry=="day of week":
                from day_of_week_datme import dow
                dow()
            elif qry=="day of month":
                from day_of_month_datme import dom
                dom()
            elif qry=="day of year":
                from day_of_year_datme import doy
                doy()
        elif ask=="table":
            alu=18
            while alu==18:
                from menu_tabe import enu
                enu()
                reqt = input("what do you want to do with the table ")
                if reqt == "alter":
                    from alter_tabe import alr
                    alr()
                elif reqt=="back":
                    alu+=18
                elif reqt=="blend":
                    from blend_tabe import bld
                    bld()
                elif reqt=="concat":
                    from concat_tabe import cot
                    cot()
                elif reqt=="create": #ma'am
                    from create_tabe import cet
                    cet()
                elif reqt=="delete":
                    from delete_tabe import dlet
                    dlet()
                elif reqt=="desc":
                    from desc_tabe import dsc
                    dsc()
                elif reqt=="display":
                    from display_tabe import dly
                    dly()
                elif reqt=="having":
                    from having_tabe import hig
                    hig()
                elif reqt=="index":
                    from index_tabe import idx
                    idx()
                elif reqt=="insert": #ma'am
                    from insert_tabe import ist
                    ist()
                elif reqt=="join":
                    from join_tabe import jin
                    jin()
                elif reqt=="order":
                    from order_tabe import odr
                    odr()
                elif reqt=="remove table":
                    from remove_table_tabe import rove
                    rove()
                elif reqt=="see tables":
                    from see_table_tabe import sele
                    sele()
                elif reqt=="see values":
                    from see_values_tabe import slu
                    slu()
                elif reqt=="table syntax":
                    from table_syntax_tabe import tey
                    tey()
                elif reqt=="update":
                    from update_tabe import udte
                    udte()
                
                    
                    
                
