# Q36. I would like to be able to pass an array with two elements
#  to my swapValues function to
# swap the values. However it appears that the values aren't changing.
# Can you figure out what's wrong here?

# def array(a):
#     for i in range(0,len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]==a[j]:
#                 print(a[j])
# array([1,4,5,4,3,2,7,8,9,6])                

def array(a,b):
    c=a
    a=b
    b=c
    print(a)
    print(b)
a=int(input("enter a"))
b=int(input("enter b"))
array(a,b)    