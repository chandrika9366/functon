# Q4.Write a Python program to reverse a string.
# "1234abcd"
def string(a):
    i=len(a)-1
    while i>=0:
        print(a[i],end="")
        i-=1
string("1234abcd") 