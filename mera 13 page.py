# You have to define a function named students and pass a parameter 
# to that function which takes a list of students name(don't use the List)
def student_name(*name):
     print(name)
student_name("chandrika","priyatam","kimpi")

# You have to define a function named isGreaterThan20 in which you 
# have to pass two parameters to the function and the first parameter 
# by default should be 20.And then output should be True if both 
# values are greater than 20 and False if any one is equal 
# to 20 or less than 20.
def greaterthan():
    a=int(input("enter a"))
    b=int(input("enter b"))
    if a>b:
        return a 
    elif a<b:
        return b 
    else:
        return "equal" 
print(greaterthan())               
