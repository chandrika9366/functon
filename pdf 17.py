# Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting
# to be 18. )
def vote():
    a=int(input("enter a"))
    if a>=18:
        print("she is able vote",a)
    else:
        print("she is not able vote",a) 
vote()           