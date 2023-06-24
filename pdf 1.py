# Q1.Write a Python program to count the number of strings where the string length is 2
# the first and last characters are the same from a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221']
def character(a):
    count=0
    x=0
    for x in a:
        if x[0]==x[-1]:
            print("first and last character same:",x)
            count+=1
    print(count)
character(['abc', 'xyz', 'aba', '1221'])            