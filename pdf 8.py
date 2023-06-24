# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12
def cnt_chr():
    string='The quick Brow Fox'
    length=len(string)
    u_cnt=0
    l_cnt=0
    for i in range(0,length):
        if string[i].isalpha()==True:
            if string[i].isupper()==True:
                u_cnt+=1
            elif string[i].islower()==True:
                l_cnt+=1
    print("No. of Uppercase characters :",u_cnt)
    print("No. of lowercase characters :",l_cnt)
cnt_chr()    
                        