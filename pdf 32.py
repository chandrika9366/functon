# Q32.Complete the function that takes a non-negative integer n as input, 
# and returns a list of
# all the powers of 2 with the exponent ranging from 0 to n (inclusive).
# n=0 == >[1] #[2^0]
# n = 1 ==> [1, 2] # [2^0, 2^1]
# n = 2 ==> [1, 2, 4] # [2^0, 2^1, 2^2].
def power():
    a=int(input("enter a"))
    j=[]
    i=0
    while i<=a:
        b=2**i
        j.append(b)
        i+=1
    print(j)
power()       