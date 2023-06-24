# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
def square(a,b):
    k=[]
    j=[]
    i=0
    while i<len(a):
        c=a[i]*a[i]
        d=b[i]*b[i]
        i+=1
        k.append(c)
        j.append(d)
    print(k,j)
square([1,2,3,4,5], [26,27,28,29,30])