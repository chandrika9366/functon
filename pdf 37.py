# Q37. Consider an array/list of sheep where some sheep may 
# be missing from their place. Weneed a function that counts the 
# number of sheep present in the array (true means present).
# For example,
# [True, True, True, False,
# True, True, True, True ,
# True, False, True, False,
# True, False, False, True ,
# True, True, True, True ,
# False, False, True, True]
# The correct answer would be 17.Hint: Don't forget to check 
# for bad values like null/undefined.

def count_sheep(sheep):
    count=0
    i=0
    while i<len(sheep):
        if sheep[i]=="True":
            count+=1   
        if count==17:  
          print("sheep present",count)
        i+=1  
count_sheep([True, True, True, False,
True, True, True, True ,
True, False, True, False,
True, False, False, True ,
True, True, True, True ,
False, False, True, True])                    
