# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(a):
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i],end=",")
        i+=1
even([1, 2, 3, 4, 5, 6, 7, 8, 9])    