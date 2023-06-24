# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update
# each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1
# Sample Input:
# 23
# 42
# 41
# 1
# Sample Output:
# -234200
# -41
# -1
def number():
    i=1
    while i<=10:
        a=int(input("enter a"))
        if a%2==0:
            print("even",a*100)
        else:
            print("odd",a*-1)
        i+=1   
number()                


