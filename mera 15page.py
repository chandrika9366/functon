# Write a function named check_numbers which takes two numbers 
# and then print "both are even" if both numbers are even 
# (divide by 2) otherwise print "both numbers are not even".
#output:
# If both numbers are even
# both are even
# If both numbers are not even
# both intergers are not even

def check_number():
    if num1==num2 and num1%2==0 and num2%2==0:
        print("If both numbers are even")
    else:
        print("both numbers are not even")
num1=int(input("enter num1"))
num2=int(input("enter num2"))        
check_number()           


# Now write a function named check_numbers_list Which takes the 
# list of an integer as a argument and then checks whether both 
# the integers with the same index are even or not.
# To check this, use the check_numbers function written in the 
# previous Part 1.
# If you call your function [2, 6, 18, 10, 3, 75] and
# [2, 6, 18, 10, 3, 75] then it should give this output:
# If the integers on same index are even
# Both intergers are even.
# If the integers on same index are not even
# Both intergers are not even

# def check_number(num1,num2):
#     i=0
#     while i<len(num1):
#         if num1[i]==num2[i]:
#             return "if the integers on same index are even"
# print(check_number([2, 6, 18, 10, 3, 75],[2, 6, 18, 10, 3, 75]))       