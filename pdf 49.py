# Q49. Write a flowchart which takes an input N. Then input N 
# numbers. Then for each of the N numbers, print“even” if the 
# number is even or and “odd” if the number is odd.
# Sample input:
# 7
# 1
# 4
# 23
# 95
# 1203
# 403
# 84
# Sample output:
# Odd
# Even
# Odd
# Odd
# OddOdd
# Even
def function(n):
    if n%2==1:
        print("odd")   
    else:
        print("even") 
n=int(input("enter n"))
function(n)              
