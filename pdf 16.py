# Q16.Print multiplication table of 12 using function.
def table():
    a=int(input("enter a"))
    i=0
    while i<=a:
        b=a*i
        i+=1
    print(b)
table()        