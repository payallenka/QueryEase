def albra():
    a=int(input("enter the coefficient of variable with power 2: "))
    b=int(input("enter the coefficient of variable with power 1: "))
    c=int(input("enter the constant value: "))
    d=-b
    e=b**2
    f=-4*a*c
    import math
    g=math.sqrt(e+f)
    h=2*a
    x=(d+g)/h
    y=(d-g)/h
    print("the values of x are as follows")
    print(x)
    print(y)

def decode():
    try:
        h=dict()
        h["0"]=-36
        h["9"]=-35
        h["8"]=-34
        h["7"]=-33
        h["6"]=-32
        h["5"]=-31
        h["4"]=-30
        h["3"]=-29
        h["2"]=-28
        h["1"]=-27
        h["`"]=-26
        h["~"]=-24
        h["/"]=-23
        h["."]=-22
        h[","]=-21
        h[">"]=-20
        h["<"]=-19
        h["''"]=-18
        h[";"]=-17
        h[":"]=-16
        h["-"]=-15
        h["="]=-14
        h["+"]=-13
        h["_"]=-12
        h[")"]=-11
        h["("]=-10
        h["*"]=-9
        h["&"]=-8
        h["^"]=-7
        h["%"]=-6
        h["$"]=-5
        h["#"]=-4
        h["@"]=-3
        h["!"]=-2
        h["?"]=-1
        h[0]=" "
        h[1]="A"
        h[2]="B"
        h[3]="C"
        h[4]="D"
        h[5]="E"
        h[6]="F"
        h[7]="G"
        h[8]="H"
        h[9]="I"
        h[10]="J"
        h[11]="K"
        h[12]="L"
        h[13]="M"
        h[14]="N"
        h[15]="O"
        h[16]="P"
        h[17]="Q"
        h[18]="R"
        h[19]="S"
        h[20]="T"
        h[21]="U"
        h[22]="V"
        h[23]="W"
        h[24]="X"
        h[25]="Y"
        h[26]="Z"
        x=[]
        acc=int(input("enter the number of elements "))
        print()
        print("from left to right")
        print()
        while acc>0:
            b=int(input("enter one by one element "))
            x.append(b)
            acc-=1
        d=[0,0,1,0,-1,-1,1,2,1]
        f=[] #first element
        for r in range(0,len(x),3):
            for t in range(0,9,3):
                f.append(x[r]*d[t])
        w=[] #second element
        for r in range(1,len(x),3):
            for t in range(1,9,3):
                w.append(x[r]*d[t])
        v=[] #third element
        for r in range(2,len(x),3):
            for t in range(2,9,3):
                v.append(x[r]*d[t])
        m=[]
        for i in range(0,len(f)):
            m.append(f[i]+w[i]+v[i])
        print()
        print("CODE DECODED")
        print()
        for u in m:
            print(h[u],end=" ")
    except:
        print("something went wrong:")
    
def encode():
    try:
        h=dict()
        h["0"]=-36
        h["9"]=-35
        h["8"]=-34
        h["7"]=-33
        h["6"]=-32
        h["5"]=-31
        h["4"]=-30
        h["3"]=-29
        h["2"]=-28
        h["1"]=-27
        h["`"]=-26
        h["~"]=-24
        h["/"]=-23
        h["."]=-22
        h[","]=-21
        h[">"]=-20
        h["<"]=-19
        h["''"]=-18
        h[";"]=-17
        h[":"]=-16
        h["-"]=-15
        h["="]=-14
        h["+"]=-13
        h["_"]=-12
        h[")"]=-11
        h["("]=-10
        h["*"]=-9
        h["&"]=-8
        h["^"]=-7
        h["%"]=-6
        h["$"]=-5
        h["#"]=-4
        h["@"]=-3
        h["!"]=-2
        h["?"]=-1
        h[" "]=0
        h["A"]=1
        h["B"]=2
        h["C"]=3
        h["D"]=4
        h["E"]=5
        h["F"]=6
        h["G"]=7
        h["H"]=8
        h["I"]=9
        h["J"]=10
        h["K"]=11
        h["L"]=12
        h["M"]=13
        h["N"]=14
        h["O"]=15
        h["P"]=16
        h["Q"]=17
        h["R"]=18
        h["S"]=19
        h["T"]=20
        h["U"]=21
        h["V"]=22
        h["W"]=23
        h["X"]=24
        h["Y"]=25
        h["Z"]=26
        q=input("enter your message to be encoded ") #message
        import string
        w=q.upper()
        l=[]
        for i in w:
            l.append(h[i])
        #print(len(l))
        while len(l)%3!=0:
            if len(l)%3!=0:
                l.append(0)
        g=[1,2,1,-1,-1,0,1,0,0]
        f=[] #first element
        for r in range(0,len(l),3):
            for t in range(0,9,3):
                f.append(l[r]*g[t])
        k=[] #second element
        for r in range(1,len(l),3):
            for t in range(1,9,3):
                k.append(l[r]*g[t])
        p=[] #third element
        for r in range(2,len(l),3):
            for t in range(2,9,3):
                p.append(l[r]*g[t])
        m=[]
        for i in range(0,len(p)):
            m.append(f[i]+k[i]+p[i])
        v=int(len(m)/3)
        et=2
        print()
        print("HERE IS YOUR CODE")
        print()
        #for i in range(0,len(m)):
        #    print(m[i],end="    ")
        #    if i==et:
        #        print("\n")
        #        et+=3
        for yu in m:
            print(yu,end=" ")
        print()
        print("number of elements = ",len(m))
    except:
        print("something went wrong:")
            
encode()   
        
    
    
