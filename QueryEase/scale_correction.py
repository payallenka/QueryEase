x=int(input("enter vale of temperature in farenheit"))
y=int(input("enter the error in the scale that has to be deduced"))
def temp(f,e):
    yu=f-e
    return yu
def accu(a,b):
    global d
    k=temp(a,b)
    d=((k-32)*5)/9
    return d

accu(x,y)
z=round(d,2)
print()
print("the accurate value of the temperature in celcius is ",d,"or can be rounded of to ",z)    
print("the accurate value of temperature in farenheit is ",temp(x,y))
