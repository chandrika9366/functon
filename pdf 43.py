# Q43. Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. 
# Print the last ‘N’ elements of the given list. ‘N’ is accepted 
# from the user.
# Sample Input:
# 1
# Sample Output:
# q
# Sample Input:
# 3
# Sample Output:
# 5
# b
# q
def function(n):
    i=0
    a=["a","1","2","5","b","q"]
    while i<len(a):
        b=a[-n:]
        i+=1    
    print(b) 
n=int(input("enter n")) 
function(n)     