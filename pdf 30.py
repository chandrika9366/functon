# Q30. Write a function that prints all the prime numbers between 
# 0 and limit where limit is a parameter.
def prime(limit):
    i=0
    a=2
    while i<a//2:
        if i%a==0:
            print("it is not prime")
            break
        i+=1
    else:
        print("it is prime")
limit=int(input("enter limit"))        
prime(limit)