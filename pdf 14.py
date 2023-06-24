# Q14.Write a function to check if a number is prime or not.
def prime():
    a=int(input("enter a"))
    i=2
    while i<a//2:
        if a%i==0:
            print("not prime",a)
            break
        i+=1
    else:
        print("prime",a) 
prime()           