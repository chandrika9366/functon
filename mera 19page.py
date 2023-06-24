def calculator(num1,num2,operator):
    if operator=="+":
       print(num1+num2,"it's add")
    elif operator=="-":
       print(num1-num2,"it's sub")   
    elif operator=="*":
       print(num1*num2,"it is multiply")  
    elif operator=="//":
      print(num1//num2,"it is floor")  
    elif operator=="**":
       print(num1**num2,"it is exponent")    
    else:
      print(num1/num2,"it is divide")   
operator=input(" select the operation")      
num1=int(input("enter num1"))
num2=int(input("enter num2"))
calculator(num1,num2,operator)         