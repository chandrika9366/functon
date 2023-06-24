# Q44.Bonus - Given the same list, print the last ‘N’ elements 
# erse order.
# Sample Input:
# 2
# Sample Output:
# q
# b
# Sample Input:
# 3
# Sample Output:
# q
# b
# 5
def function(n):
    i=0
    a=["a","1","2","5","b","q"]
    while i<len(a):
        b=a[-n:]
        b.reverse()
        i+=1    
    print(b) 
n=int(input("enter n")) 
function(n)  