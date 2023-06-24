# Write a function named add_numbers_list which takes 2 lists of 
# two integers and then prints the sum of the integers with the same position.

# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this

def add_number(a,b):
    i=0
    c=[]
    while i<len(a):
        l=a[i]+b[i]
        c.append(l)
        i+=1
    print(c)
add_number([50,60,10],[10,20,13])  

# Write a function named add_numbers which takes two numbers as 
# arguments and then prints their sum. The name of the arguments 
# should be number1 and number2.
def add_number(num1,num2):
    print(num1+num2)
add_number(56,12)    

