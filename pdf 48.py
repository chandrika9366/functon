# Q48. Two numbers are entered through the keyboard. 
# Write a flowchart to find the value of the
# raised to the power of another.
# Sample Input
# 3
# 4
# Sample Output
# 81 (3x3x3x3)
# first number
def power(a,b):
    while a<=b:
        k=a**b
        return k
print(power(3,4))       
