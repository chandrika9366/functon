# Q46. Draw a flowchart to take a list of N numbers from the 
# user, print True if the complete list consists ofconsecutive 
# numbers with a difference of one. Print False otherwise.
# Sample Input:
# 1 2 3 4 5 6 7
# Sample Output:
# True
# Sample Input:
# 45 46 47 48 49 51 52
# Sample Output:
# False
def function(n):
    for i in range(1,n+1):
        if n[i]==a[i]:
            return "True"
        else:
            return "False"   
a=int(input("enter a"))
print(function(a))           