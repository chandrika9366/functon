# def ascending(a):
# 	i=0
# 	while i<len(a):
# 	    a.sort()
#         i+=1
#     print(a)    
# ascending([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])

# a=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# i=0
# while i<len(a):
#     a.sort()
#     i+=1
# print(a)  
st="malayalam"
for i in range(0,int(len(st)/2)):
    if st[i]==st[len(st)-i-1]:
        print("palindrome")
    else:    
      print("not palindrome")          
